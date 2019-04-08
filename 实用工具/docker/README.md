# Docker

* [实例](#实例)
* [镜像](#镜像)
* [容器](#容器)
* [DockerFile](#DockerFile)
* [服务器](#服务器)

---
# 实例
```
docker ps
```
# 镜像
1. 拉取一个镜像
```
docker pull image_name
```
2. 查看所有镜像/某个镜像
```
docker images

docker images image_name
```
# 容器
1. 运行一个容器
```
docker run -d -p 80:80 image_name
```
* 参数
   * -d: 后台
   * -p: 端口映射 docker容器：host端口
   * -i: 交互式
   * -t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用
   * --nam: 要在run --name 其他参数
> 为啥在最后加上/bin/bash：(启动容器后启动bash)
>> docker中必须要保持一个进程的运行，要不然整个容器就会退出


> 在有DockerFile的目录下（✘别忘了后面的 .）
```
docker build -t image_name .
```
# DockerFile
```
FROM python:3.6.6
ARG config
ENV TZ Asia/Shanghai

COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple/ -r /tmp/requirements.txt
COPY ./config/__init__.py ./config/${config}.ini ${target}/config/
COPY app.py ${target}/app.py
```
* 参数
   * FROM <image>:<tag> → 在某个镜像上构建
   * ARG → 指定构建时的变量
   * ENV → 设置环境变量
   * COPY → 
# 服务器
> 默认情况下，只允许本地客户端请求
```
# 允许远程客户端请求

# Ubuntu
vim /etc/systemd/multi-user.target.wants/docker.service
```
