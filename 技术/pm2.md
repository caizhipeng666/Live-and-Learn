# PM2

* [安装](#安装)
* [使用](#使用)

### 安装
```
sudo apt-get install nodejs
sudo apt install nodejs-legacy
sudo npm install -g pm2
```
> -g 全局

```
sudo npm config set registry https://registry.npm.taobao.org
```
> 切换源,否则巨慢

```
sudo npm install -g pm2
```

### 使用
1. 写好shell脚本/ json配置

* shell
```
#!/bin/sh
set -e
source ./venv/bin/activate
export DJANGO_SETTINGS_MODULE="项目.settings"
python3 manage.py runscript xxx_xxx
```
> set -e 告诉bash如果任何语句的执行结果不是true则应该退出   
> source 到虚拟环境时:
>> 如果没有虚拟环境 python -m venv 虚拟环境文件夹名

* json
```
```

2. 载入
```
pm2 start xxx.sh
```
