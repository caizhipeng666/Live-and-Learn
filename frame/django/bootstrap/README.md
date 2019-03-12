# 导入BootStrap
---
### 下载css和js(官方文档中选择下载)
> https://v3.bootcss.com/

### settings.py中添加静态文件配置
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
                                                 ↑文件夹名   
### 模版文件中引入bootstrap
```
{% load staticfiles %}
<link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
<link rel="stylesheet" href="{% static 'bootstrap/js/bootstrap.min.js' %}">
```

### 目前不知道有什么用的jquery
```
<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
```
