# Docker

* [实例](#实例)
* [镜像](#镜像)
* [容器](#容器)

---
# 实例
```
docker ps
```
# 镜像
```
docker images
```
# 容器
1. 运行一个容器
```
docker run -d -p 80:80 image
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
docker build -t 镜像名称 .
```
