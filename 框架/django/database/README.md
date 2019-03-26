方法 | 说明
--- | ---
[多数据库](#多数据库) | 配置&使用
[加悲观锁](#加悲观锁) | select_for_update()
[数据库连接](#数据库连接数处理) | django.db.close_old_connections()
---

# 多数据库
1. setting中添加多数据库
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'info': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'user_info',
        'USER': 'root',
        'PASSWORD': DATABASES_PW,
        'HOST': '192.168.247.128',
        'PORT': '3306'
    }
}
```

2. setting中添加数据库分配
```python
# 数据库Router
DATABASE_ROUTERS = ['app.写在某个py.某个Router类']
# 数据库分配
DATABASE_APPS_MAPPING = {
    'account': 'info',
    'comment': 'info',
    'place': 'info'
}
```

3. 编写Router类,新增一个py
```python
from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class DatabaseAppsRouter(object):
    """
    A router to control all database operations on models for different
    databases.

    In case an app is not set in settings.DATABASE_APPS_MAPPING, the router
    will fallback to the `default` database.

    Settings example:

    DATABASE_APPS_MAPPING = {'app1': 'db1', 'app2': 'db2'}
    """

    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def db_for_write(self, model, **hints):
        """Point all write operations to the specific database."""
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # 当 obj1 和 obj2 之间允许有关系时返回 True ，不允许时返回 False ，或者没有 意见时返回 None
        """Allow any relation between apps that use the same database."""
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None

    def allow_syncdb(self, db, model):
        # 决定 model 是否可以和 db 为别名的数据库同步
        """Make sure that apps only appear in the related database."""

        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None
```

4. 更新数据库
```python
python manage.py migrate --database=info
```
---

# 加悲观锁
```python
queryset.objects.select_for_update()
```

# 数据库连接数处理
```
# django ORM中用到的数据库连接来源
connections = ConnectionHandler()

# 请求开始之前重置所有连接
def reset_queries(**kwargs):
    for conn in connections.all():
        conn.queries_log.clear()
signals.request_started.connect(reset_queries)

# 请求开始结束之前遍历所有已存在连接，关闭不可用的连接
def close_old_connections(**kwargs):
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()
signals.request_started.connect(close_old_connections)
```
