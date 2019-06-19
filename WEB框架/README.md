# By 2019/6/12

框架|问题|原因|跳转
---|---|---|---
Django|request.META.get()获取不到信息|nginx在处理时会自己加上http|[1](#1)
Django|test创建数据库时编码问题|docker创建的mysql默认编码为latin|[2](#2)

# 1
### Django-request.META.get()获取不到信息
> 发送方
```python
# 注意DJANGO META中的_要用-处理
headers = {
    'XXX-TOKEN': token
}
res = requests.get(url=api_url, headers=headers, params=params)
```
> 接收方
```python
if request.META.get('HTTP_XXX_TOKEN') != settings.RISK_TOKEN:
    return HttpResponse('INVALID TOKEN !', status=401)
```
![](./image/Django_META.png)

# 2
### test创建数据库时编码问题
##### docker-compose.yml
```
  czp_mysql:
    image: mysql:5.7
    environment:
        ...
    volumes:
      - .:/etc/mysql/conf.d
```
##### mysql.cnf
```
[mysqld]
```
character-set-server=utf8
##### Django.settings
```pyton
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'czp_mysql',
        'PORT': 3306,
        'NAME': 'czp',
        'USER': 'root',
        'PASSWORD': '123456',
        'TEST_CHARSET': 'utf8mb4',
        'TEST_COLLATION': 'utf8_general_ci',
        'OPTIONS': {
            'charset': 'utf8mb4',
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
```
### 补充一个外键创建可能：
num|description|Example\解决
---|---|---
1|两个字段的类型或者大小不严格匹配|如果一个是INT(10), 那么外键也必须设置成INT(10)
2|你试图引用的其中一个外键没有建立起索引，或者不是一个primary key|如果其中一个不是primary key 的，你必须为它创建一个索引。
3|外键的名字是一个已经存在的一个键值了|这个时候，你应该检查你的数据库以确保外健名字是唯一的，或者你在键名后面加上几个随机的字符以测试是否是这个原因 
4|其中一个或者两个表是MyISAM引擎的表，若想要使用外键约束，必须是InnoDB引擎|
5|设置了ON DELETE SET NULL, 但相关的键的字段设置成了NOT NULL|通过修改cascade 的属性值或者把字段属性设置成allow null来搞定这个bug 
6|请确定你的Charset 和 Collate 选项在表级和字段级上的一致
7|你可能设置为外键设置了一个默认值|default=0
8|在这个关系里面，其中的一个字段是一个混合键值中的一个，它没有自己独立的索引|这时，你必须为它创建一个独立的索引。
9|ALTER 声明中有语法错误
