# Redis

* [安装](#安装)
* [使用](#使用)

# 安装
1. 获取服务器
```
sudo apt-get install redis-server
```
2. 查看状态
```
# 查看进程
ps -aux|grep redis

# 查看服务
netstat -nlt|grep 6379

#访问redis
redis-cli
```
3. redis设置
1. △设置成密码登录
```
sudo vi /etc/redis/redis.conf
找到 # requirepass foobared这行
改成 
requirepass 你的密码
```
2. △设置成远程可访问
```
sudo vi /etc/redis/redis.conf
找到 bind 127.0.0.1这行,注释掉
#bind 127.0.0.1
```
3. 重启服务
```
sudo /etc/init.d/redis-server restart
```
---
# 使用
方法|
---|
[登录](#登录)|

---
### 登录
1. 本地
```
redis-cli -a 密码
```
2. 远程
```
redis-cli -a 密码 -h ip地址
```
### 基本命令
> [常用](http://doc.redisfans.com/)

