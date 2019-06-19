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
```
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
