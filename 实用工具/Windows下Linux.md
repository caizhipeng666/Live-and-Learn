Windows玩转Linux子系统

# 开发模式
```
左下角设置 → 更新和安全 → 开发者选项
```

# 控制面板添加子系统
```
控制面板 → 程序 → 适用Linux子系统
```

# 应用商店下载Ubuntu

# 打开Ubuntu
### 生成ssh Key
```
ssh-keygen -t rsa -C "czp@xxx.com"
```
### 换上阿里云镜像
> vim /etc/apt/sources.list
```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse 
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse 
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse 
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse 
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse 
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse 
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse 
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse 
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse 
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```
### 更新下Ubuntu
```
sudo apt-get update
```
