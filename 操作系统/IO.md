# 一次I/O
```
1.等待数据,将数据从网络/磁盘拷贝到系统kernel的缓冲区
2.将数据从kernel拷贝到进程中
```

# 五种I/O
```
1.阻塞I/O模型

2.非阻塞I/O模型

3.I/O复用模型
   1.select/poll
   2.epoll

4.信号驱动I/O模型

5.异步I/O模型
```

# I/O多路复用与异步I/O
1. I/O多路复用

```
    锁住整个进程，不断轮询所有socket(套接字是不被block的),
    同时，kernel会监视所有select负责的socket，(注册多个socket，不断地调用select读取被激活的socket)
    当任何一个socket中的数据准备就绪，select就会返回。这时进程再调用read操作(第二步)。
```

> 在处理更多连接数的时候,性能比较卓越;(在同一个线程内同时处理多个IO请求的目的)   
> 反之,在处理较少连接数时,延迟可能更大,不如异步I/O

2. 异步I/O

```
    进程发起I/O请求之后,直接去做其他的事情了。
    此时,kernel收到请求后,会立刻返回，不会对进程有任何的block，
    但它会等待数据准备完成，然后将数据拷贝到用户内存，当一切都做好了再返回进程一个singal
```

> 少了去查询IO状态的这部分,且在整个过程中是不加锁的

