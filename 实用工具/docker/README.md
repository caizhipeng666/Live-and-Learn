# Docker

* [实例](#实例)
* [镜像](#镜像)
* [容器](#容器)
* [DockerFile](#DockerFile)
* [服务器](#服务器)
* [仓库](#仓库)

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
   * -p: 端口映射 host端口：docker镜像端口
   * -i: 交互式
   * -t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用
   * --nam: 要在run --name 其他参数
> 为啥在最后加上/bin/bash：(启动容器后启动bash)   
>>      docker中必须要保持一个进程的运行，要不然整个容器就会退出

2. 构建一个新容器(要先运行一个容器)
```
docker commit image_name new_name
```

3. 进入容器
```
docker attach -it ps_id bash
docker exec ps_id
```
> exec是打开新的终端，会启动新的进程

4. 查看容器输出
```
docker logs -f ps_id
```

5. 容器操作
```
docker stop/start/restart ps_id
```
* 参数
   * --restart=always   任何原因退出都立即重启
   * --restart=on-failure:3   退出代码非0时，最多重启3次 
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
   * ENV → 设置环境变量 ($ENV_name就可以检测)
   * COPY → 将本地文件添加到容器中
     > COPY hom?.txt /mydir/      # ? 替代一个单字符,如："home.txt" 到 /mydir/
   * RUN command param1 param2→ 构建容器时调用
   * WORKDIR → 工作目录
   * CMD → 构建容器后默认调用(多个CMD指令，也只会运行最后那个)
     > ✓当CMD后面有RUN命令的时候，CMD将被忽略
   * ENTRYPOINT → 容器启动时调用(RUN和CMD的传参会给到它，多个ENTRYPOINT只会运行最后那条)
> 可以用docker history image_name 查看构建历史

# 服务器
> 默认情况下，只允许本地客户端请求
```
# 允许远程客户端请求

# Ubuntu
vim /etc/systemd/multi-user.target.wants/docker.service
```

# 仓库
> Docker Hub可以被别人访问
```
docker login -u dockerID
```
### 重命名镜像 --- 格式为 dockerID/xxx:tag
```
docker tag image_name czp/image_name:v1
```
> 去掉后面的tag的话，就会上传全部镜像层
### 发布
```
docker push czp/image_name:v1
```
### 搭建本地仓库
```
docker run -d -p 5000:5000 -v /myregistry:/var/lib/registry registry:czp
```
* 参数：
   * -v：挂载目录
```
docker tag czp/image_name:v1 registry-host:5000/czp/image_name:v1

docker push registry-host:5000/czp/image_name:v1

docker pull registry-host:5000/czp/image_name:v1
```
