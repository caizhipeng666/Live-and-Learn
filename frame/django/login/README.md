# 用户登录
---
模块|说明
---|---
[数据表](#数据表)|user表结构
[登录](#登录)|登入、登出
[登录状态](#登录状态)|登录状态判定
---

# 数据表
```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 除了自带字段外, 添加自定义字段
    telephone = models.CharField('手机', max_length=11)
    nickname = models.CharField('昵称', max_length=16)
```
---

# 登录
```python
from django.contrib.auth import authenticate, login, logout

user = authenticate(username='xxx', password='xxxxx')
login(request, user)
logout(request)
```

# 登录状态
1. 判断是否登录/活跃
```python
if request.user.is_authenticated:
if request.user.is_active:
```
2. 需要登录才可以进入的视图
```python
@login_required
@login_required(redirect_field_name='url_name')
@login_required(login_url='/xxx/xxx')

补充一个reverse的使用, reverse('url_name') = login_required的redirect_field_name='url_name'
```