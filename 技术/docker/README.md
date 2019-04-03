# Docker

* [概念](#概念)

* 使用

---
# 概念

* docker容器是完全使用沙箱机制，相互之间不会有任何接口   
> 一个做好的应用容器长得就好像一个装好了一组特定应用的虚拟机一样。
```
比如我现在想用MySQL那我就找个装好MySQL的容器，运行起来，那么我就可以使用MySQL了。
而且一旦你想换台机器，直接把这个容器端起来，再放到另一个机器就好了。硬件，操作系统，运行环境什么的都不需要考虑了。
若果利用容器的话，那么开发直接在容器里开发，提测的时候把整个容器给测试，
测好了把改动改在容器里再上线就好了。通过容器，整个开发、测试和生产环境可以保持高度的一致。   
```

* Docker守护进程可以直接与主操作系统进行通信，为各个Docker容器分配资源
> 它将容器与主操作系统隔离，并将各个容器互相隔离。   
> 虚拟机启动需要数分钟，而Docker容器可以在数毫秒内启动。由于没有臃肿的从操作系统，Docker可以节省大量的磁盘空间以及其他系统资源。

* Docker Engine+docker hub = docker platform   
> docker引擎是一个c/s结构的应用， 是一个基于虚拟化技术的轻量级并且功能强大的开源容器引擎管理工具。   
> 它可以将不同的 work flow 组合起来构建成你的应用   

![](images/engine.png "")
### Docker Daemon(服务端)
```
Docker架构中常驻后台的系统进程，是一个服务进程，负责接收处理用户发送的请求和管理所有的Docker容器
```
> 所谓的运行Docker即代表运行Docker Daemon。
### Docker Client(客户端)
```
Docker架构中用户与Docker Daemon建立通信的客户端。
```
> 扮演着docker服务端的远程控制器，可以用来控制docker的服务端进程。   
> 大部分情况下，docker服务端和客户端运行在一台机器上。   
---
* Docker内部构建
   * Docker 镜像 - Docker images
   ```
       docker pull     //从网络上下载镜像
       docker images  //查看本地主机已经存在的镜像 
   ```
   > 镜像=操作系统+软件运行环境+用户程序

   * Docker 仓库 - Docker registeries

   * Docker 容器 - Docker containers
   > 镜像可以用来创建Docker容器，一个镜像可以创建很多容器   
![](images/container.jpg "")
---
* DockerFile
* Docker Compose
   > Docker Compose是Docker容器进行编排的工具，定义和运行多容器的应用，可以一条命令启动多个容器。
   1. Dockerfile 定义应用的运行环境
   2. Docker-compose.yml 定义组成应用的各服务
   3. Docker-compose up 启动整个应用
# 
```
docker ps
```
```
docker images
```
> 在有DockerFile的目录下（✘别忘了后面的 .）
```
docker build -t 镜像名称 .
```
