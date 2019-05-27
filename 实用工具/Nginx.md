# Nginx

* [安装](#安装)
* [配置](#配置)

# 安装
1. Ubuntu
```
sudo apt-get install nginx

/usr/sbin/nginx：主程序
/etc/nginx：存放配置文件
/usr/share/nginx：存放静态文件
/var/log/nginx：存放日志

sudo service nginx start
```
> 检测有无安装成功: whereis nginx   
> Nginx的配置 → → /etc/nginx/nginx.conf

# 配置
1. 添加conf
```
sudo vim /etc/nginx/sites-available/xxx.conf
```
2. 不知道有没用(激活)
```
sudo ln -s /etc/nginx/sites-available/xxx.conf /etc/nginx/sites-enabled/xxx.conf
```
3. 测试配置
```
sudo service nginx configtest

或

进入nginx安装目录sbin下，输入命令./nginx -t
```
4. 重启
```
sudo service nginx restart
```


gunicorn
```
gunicorn -w4 -b0:8080 xxx.wsgi
```
