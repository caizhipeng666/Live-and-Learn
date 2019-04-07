# Gunicorn

* [安装](#安装)
* [使用](#使用)

# 安装
```
sudo pip install gunicorn
```

# 使用
```
gunicorn -w4 -b0.0.0.0:8001 项目.wsgi
```
* -w 表示开启多少个worker，
* -b 表示要使用的ip和port，
> 0.0.0.0代表监控电脑的所有 ip
