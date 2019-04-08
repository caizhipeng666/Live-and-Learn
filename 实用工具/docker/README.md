# Docker

* [实例](#实例)
* [镜像](#镜像)
* [容器](#容器)
* [DockerFile](#DockerFile)
* [服务器](#服务器)

---
# 实例
```
docker ps -a
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

3. 通过DockerFile构建一个镜像
> 在有DockerFile的目录下（✘别忘了后面的 .）
```
docker build -t image_name .
```
* 参数
   * -f：指定DockerFile位置
> 当docker执行某一步失败时：
>>     可以通过docker run -it 去启动一下镜像，会在错误的那一步停止&报错   
   
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
>>      docker中必须要保持一个进程的运行，要不然整个容器就会退出

2. 构建一个新容器(要先运行一个容器)
```
docker commit image_name new_name
```

# DockerFile
```
FROM python:3.6.6
ARG config
ENV TZ Asia/Shanghai

COPY ./requirements.txt /tmp/
RUN pip install --no-cache-dir --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple/ -r /tmp/requirements.txt
RUN apt-get update && apt-get install -y vim
COPY ./config/__init__.py ./config/${config}.ini ${target}/config/
COPY app.py ${target}/app.py

WORKDIR ${target}
CMD python app.py ${config} --port 8080
```
* 参数
   * FROM <image>:<tag> → 在某个镜像上构建
   * ARG → 指定构建时的变量
   * ENV → 设置环境变量
   * COPY → 将本地文件添加到容器中
     > COPY hom?.txt /mydir/      # ? 替代一个单字符,如："home.txt" 到 /mydir/
   * RUN command param1 param2→ 构建容器时调用
   * WORKDIR → 工作目录
   * CMD → 构建容器后默认调用(多个CMD指令，也只会运行最后那个)
   * ENTRYPOINT → 容器启动时调用(RUN和CMD的传参会给到它，多个ENTRYPOINT只会运行最后那条)
> 可以用docker history image_name 查看构建历史

# 服务器
> 默认情况下，只允许本地客户端请求
```
# 允许远程客户端请求

# Ubuntu
vim /etc/systemd/multi-user.target.wants/docker.service
```
