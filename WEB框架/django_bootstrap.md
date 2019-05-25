# 导入BootStrap
---
### 下载css和js(官方文档中选择下载)
> https://v3.bootcss.com/

### settings.py中添加静态文件配置
    (全局情况)
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
                                                 ↑文件夹名   
                                               如果staic放在app中则app.static
### 模版文件中引入bootstrap
```
<head>
{% load staticfiles %}
<link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
</head>
<body>
<script type="text/javascript" src="{% static 'bootstrap/js/bootstrap.min.js' %}"></script>
</body>
```

### 目前不知道有什么用的jquery
```
<script src="https://cdn.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"></script>
```

### 去除图标404
```
<link rel="shortcut icon" href="图片URL(https://icons8.com/icons)" type="image/x-icon">
```
