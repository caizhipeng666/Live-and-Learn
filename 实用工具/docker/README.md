# Docker

* [镜像](#镜像)
* [容器](#容器)
* [DockerFile](#DockerFile)
* [服务器](#服务器)
* [仓库](#仓库)
* [DockerCompose](#DockerCompose)

---
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
   * --name: 要在run --name 其他参数
   * -h：让容器有自己的hostname
   
   * -m：设置内存限额 -m 200M (--memory-swap 默认为-m两倍)
   * --vm：分配线程 --vm 1 (--vm-bytes 200M 每个线程内存)
   * -c：cpu限额 (-cpu-shares权重)
   * --blkio-weight：优先级
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

4. 查看所有容器
```
docker ps -a / docker container ls -a
```

5. 容器与外界文件交互
```
docker cp image_id:/tmp host/tmp/

docker cp c://czp/ image_id:/tmp/
```

6. 查看容器输出
```
docker logs -f --tail 20 container_id
```

7. 容器操作
```
docker stop/start/restart/pause/unpause ps_id
```
* 参数
   * --restart=always   任何原因退出都立即重启
   * --restart=on-failure:3   退出代码非0时，最多重启3次 
   
7. 删除容器
```
docker rm ps_id
```
> 批量删除 docker rm -v $(docker ps -aq -f status=exited)
---

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
---
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
---
# DockerCompose
> https://docs.docker.com/compose/compose-file/
```
1. image

    services:
      web:
        image: hello-world
在 services 由用户自定义，它就是服务名称
Ex：
    image: redis
    image: ubuntu:14.04
    image: tutum/influxdb
    image: example-registry.com:4000/postgresql
    image: a4bc65fd

2. build

服务除了可以基于指定的镜像，还可以基于一份 Dockerfile，
在使用 up 启动之时执行构建任务，这个构建标签就是 build，它可以指定 Dockerfile 所在文件夹的路径
    build: /path/to/build/dir
也可以是相对路径，只要上下文确定就可以读取到 Dockerfile
    build: ./dir
设定上下文根目录，然后以该目录为准指定 Dockerfile
    build:
      context: ../
      dockerfile: path/of/Dockerfile  # 指定 Dockerfile 文件
✓同时指定了 image 和 build 两个标签，
 那么 Compose 会构建镜像并且把镜像命名为 image 后面的那个名字
    build: ./dir
    image: webapp:tag
在 docker-compose.yml 文件中也支持ARG：
    build:
      context: .
      args:
        buildno: 1
        password: secret
下面这种写法也是支持的，一般来说下面的写法更适合阅读。
    build:
      context: .
      args:
        - buildno=1
        - password=secret
与 ENV 不同的是，ARG 是允许空值的。例如：
    args:
      - buildno
      - password
    ▲注意：YAML 的布尔值（true, false, yes, no, on, off）
          必须要使用引号引起来（单引号、双引号均可），否则会当成字符串解析。

3. command

使用 command 可以覆盖容器启动后默认执行的命令。
command: bundle exec thin -p 3000
也可以写成类似 Dockerfile 中的格式：
command: [bundle, exec, thin, -p, 3000]

4.container_name

前面说过 Compose 的容器名称格式是：<项目名称><服务名称><序号>
虽然可以自定义项目名称、服务名称，但是如果你想完全控制容器的命名，可以使用这个标签指定：
container_name: app
这样容器的名字就指定为 app 了。

5.depends_on

这个标签解决了容器的依赖、启动先后的问题。
例如下面容器会先启动 redis 和 db 两个服务，最后才启动 web 服务：
    version: '2'
    services:
      web:
        build: .
        depends_on:
          - db
          - redis
      redis:
        image: redis
      db:
        image: postgres

6.dns

和 --dns 参数一样用途，格式如下：
    dns: 8.8.8.8
也可以是一个列表：
    dns:
      - 8.8.8.8
      - 9.9.9.9
此外 dns_search 的配置也类似：
    dns_search: example.com
    dns_search:
      - dc1.example.com
      - dc2.example.com

7. tmpfs

挂载临时目录到容器内部，与 run 的参数一样效果：
    tmpfs: /run
    tmpfs:
      - /run
      - /tmp

8. entrypoint

在 Dockerfile 中有一个指令叫做 ENTRYPOINT 指令，用于指定接入点，第四章有对比过与 CMD 的区别。
在 docker-compose.yml 中可以定义接入点，覆盖 Dockerfile 中的定义：
    entrypoint: /code/entrypoint.sh
格式和 Docker 类似，不过还可以写成这样：
    entrypoint:
        - php
        - -d
        - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
        - -d
        - memory_limit=-1
        - vendor/bin/phpunit

9.env_file

还记得前面提到的 .env 文件吧，这个文件可以设置 Compose 的变量。
而在 docker-compose.yml 中可以定义一个专门存放变量的文件。
如果通过 docker-compose -f FILE 指定了配置文件，则 env_file 中路径会使用配置文件路径。

如果有变量名称与 environment 指令冲突，则以后者为准。格式如下：
    env_file: .env
或者根据 docker-compose.yml 设置多个：
    env_file:
      - ./common.env
      - ./apps/web.env
      - /opt/secrets.env
注意的是这里所说的环境变量是对宿主机的 Compose 而言的，
如果在配置文件中有 build 操作，这些变量并不会进入构建过程中，
如果要在构建中使用变量还是首选前面刚讲的 arg 标签。

10. environment

与上面的 env_file 标签完全不同，反而和 arg 有几分类似，
这个标签的作用是设置镜像变量，它可以保存变量到镜像里面，
也就是说启动的容器也会包含这些变量设置，这是与 arg 最大的不同。一般 arg 标签的变量仅用在构建过程中。
而 environment 和 Dockerfile 中的 ENV 指令一样会把变量一直保存在镜像、容器中，
类似 docker run -e 的效果。

    environment:
      RACK_ENV: development
      SHOW: 'true'
      SESSION_SECRET:

    environment:
      - RACK_ENV=development
      - SHOW=true
      - SESSION_SECRET

11. expose

这个标签与Dockerfile中的EXPOSE指令一样，用于指定暴露的端口，但是只是作为一种参考，
实际上docker-compose.yml的端口映射还得ports这样的标签。
    expose:
     - "3000"
     - "8000"

12. external_links

在使用Docker过程中，我们会有许多单独使用docker run启动的容器，
为了使Compose能够连接这些不在docker-compose.yml中定义的容器，我们需要一个特殊的标签，就是external_links，
它可以让Compose项目里面的容器连接到那些项目配置外部的容器
（前提是外部容器中必须至少有一个容器是连接到与项目内的服务的同一个网络里面）。
格式如下：
    external_links:
     - redis_1
     - project_db_1:mysql
     - project_db_1:postgresql

13. extra_hosts

添加主机名的标签，就是往/etc/hosts文件中添加一些记录，与Docker client的--add-host类似：
    extra_hosts:
     - "somehost:162.242.195.82"
     - "otherhost:50.31.209.229"

启动之后查看容器内部hosts：
    162.242.195.82  somehost
    50.31.209.229   otherhost

14. labels

向容器添加元数据，和Dockerfile的LABEL指令一个意思，格式如下：
    labels:
      com.example.description: "Accounting webapp"
      com.example.department: "Finance"
      com.example.label-with-empty-value: ""
    labels:
      - "com.example.description=Accounting webapp"
      - "com.example.department=Finance"
      - "com.example.label-with-empty-value"

15. links

还记得上面的depends_on吧，那个标签解决的是启动顺序问题，这个标签解决的是容器连接问题，
与Docker client的--link一样效果，会连接到其它服务中的容器。
格式如下：
    links:
     - db
     - db:database
     - redis

使用的别名将会自动在服务容器中的/etc/hosts里创建。例如：
    172.12.2.186  db
    172.12.2.186  database
    172.12.2.187  redis

相应的环境变量也将被创建。

16. logging

这个标签用于配置日志服务。格式如下：
    logging:
      driver: syslog
      options:
        syslog-address: "tcp://192.168.0.42:123"
默认的driver是json-file。
只有json-file和journald可以通过docker-compose logs显示日志，其他方式有其他日志查看方式，但目前Compose不支持。
对于可选值可以使用options指定。
有关更多这方面的信息可以阅读官方文档：
https://docs.docker.com/engine/admin/logging/overview/

17. pid

pid: "host"
将PID模式设置为主机PID模式，跟主机系统共享进程命名空间。
容器使用这个标签将能够访问和操纵其他容器和宿主机的名称空间。

18. ports

映射端口的标签。
使用HOST:CONTAINER格式或者只是指定容器的端口，宿主机会随机映射端口。
    ports:
     - "3000"
     - "8000:8000"
     - "49100:22"
     - "127.0.0.1:8001:8001"
    注意：当使用HOST:CONTAINER格式来映射端口时，如果你使用的容器端口小于60你可能会得到错误得结果，
         因为YAML将会解析xx:yy这种数字格式为60进制。所以建议采用字符串格式。

19. security_opt

为每个容器覆盖默认的标签。简单说来就是管理全部服务的标签。比如设置全部服务的user标签值为USER。
    security_opt:
      - label:user:USER
      - label:role:ROLE

20. stop_signal

设置另一个信号来停止容器。在默认情况下使用的是SIGTERM停止容器。设置另一个信号可以使用stop_signal标签。
stop_signal: SIGUSR1

21. volumes

挂载一个目录或者一个已存在的数据卷容器，可以直接使用 [HOST:CONTAINER] 这样的格式，
或者使用 [HOST:CONTAINER:ro] 这样的格式，后者对于容器来说，数据卷是只读的，这样可以有效保护宿主机的文件系统。
Compose的数据卷指定路径可以是相对路径，使用 . 或者 .. 来指定相对目录。
数据卷的格式可以是下面多种形式：
    volumes:
      // 只是指定一个路径，Docker 会自动在创建一个数据卷（这个路径是容器内部的）。
      - /var/lib/mysql
     
      // 使用绝对路径挂载数据卷
      - /opt/data:/var/lib/mysql
     
      // 以 Compose 配置文件为中心的相对路径作为数据卷挂载到容器。
      - ./cache:/tmp/cache
     
      // 使用用户的相对路径（~/ 表示的目录是 /home/<用户目录>/ 或者 /root/）。
      - ~/configs:/etc/configs/:ro
     
      // 已经存在的命名的数据卷。
      - datavolume:/var/lib/mysql

如果你不使用宿主机的路径，你可以指定一个volume_driver。
volume_driver: mydriver

22. volumes_from

从其它容器或者服务挂载数据卷，可选的参数是 
:ro或者 :rw，前者表示容器只读，后者表示容器对数据卷是可读可写的。
默认情况下是可读可写的。
    volumes_from:
      - service_name
      - service_name:ro
      - container:container_name
      - container:container_name:rw

23. cap_add, cap_drop

添加或删除容器的内核功能。详细信息在前面容器章节有讲解，此处不再赘述。
    cap_add:
      - ALL
     
    cap_drop:
      - NET_ADMIN
      - SYS_ADMIN

24. cgroup_parent

指定一个容器的父级cgroup。
cgroup_parent: m-executor-abcd

25. devices

设备映射列表。与Docker client的--device参数类似。
    devices:
      - "/dev/ttyUSB0:/dev/ttyUSB0"

26. extends

这个标签可以扩展另一个服务，扩展内容可以是来自在当前文件，也可以是来自其他文件，
相同服务的情况下，后来者会有选择地覆盖原有配置。
    extends:
      file: common.yml
      service: webapp

用户可以在任何地方使用这个标签，只要标签内容包含file和service两个值就可以了。
file的值可以是相对或者绝对路径，如果不指定file的值，那么Compose会读取当前YML文件的信息。
更多的操作细节在后面的12.3.4小节有介绍。

27. network_mode

网络模式，与Docker client的--net参数类似，只是相对多了一个service:[service name] 的格式。
例如：
    network_mode: "bridge"
    network_mode: "host"
    network_mode: "none"
    network_mode: "service:[service name]"
    network_mode: "container:[container name/id]"

可以指定使用服务或者容器的网络。

28. networks

加入指定网络，格式如下：
    services:
      some-service:
        networks:
         - some-network
         - other-network
关于这个标签还有一个特别的子标签aliases，这是一个用来设置服务别名的标签，例如：
    services:
      some-service:
        networks:
          some-network:
            aliases:
             - alias1
             - alias3
          other-network:
            aliases:
             - alias2
相同的服务可以在不同的网络有不同的别名。

29. 其它

还有这些标签：cpu_shares, cpu_quota, cpuset, 
domainname, hostname, ipc, mac_address, 
mem_limit, memswap_limit, privileged, read_only, restart,
shm_size, stdin_open, tty, user, working_dir
上面这些都是一个单值的标签，类似于使用docker run的效果。
    cpu_shares: 73
    cpu_quota: 50000
    cpuset: 0,1
     
    user: postgresql
    working_dir: /code
     
    domainname: foo.com
    hostname: foo
    ipc: host
    mac_address: 02:42:ac:11:65:43
     
    mem_limit: 1000000000
    memswap_limit: 2000000000
    privileged: true
     
    restart: always
     
    read_only: true
    shm_size: 64M
    stdin_open: true
    tty: true
```
