# MySQL技术内幕InnoDB存储引擎
---

章节 | 内容
:---: | :---:
[1](#MySQL体系结构和存储引擎) | MySQL结构
[2](#InnoDB体系结构)| InnoDB


MySQL体系结构和存储引擎|description
---|---
1|使用NDB引擎时<br>数据库的文件可能不是操作系统上的文件,而是存放于内存中的文件
2|MySQL数据库 = 后台线程 + 一个共享内存区<br>共享内存可以被运行的后台线程所共享
3|数据库 → 文件<br>实例 → 操作数据库文件
4|△集群情况下可能存在一个数据库被多个数据实例使用
5|**MySQL是单进程多线程的**
6|MySQL可以没有配置文件(按照默认参数设置启动实例)<br>可以通过 mysql --help | grep my.cnf 来查看配置读取顺序<br>相同参数以最后一个配置文件中的参数为准
7|**MySQL插件式的存储引擎架构是与其他数据库最大的区别**
8|存储引擎是基于表的,而不是数据库
9|△InnoDB存储引擎(MVVC)<br>(1)支持事务,主要面向在线事务处理<br>(2)行锁设计、支持外键、非锁定读(默认读取操作不会产生锁)<br>(3)通过使用多版本并发控制MVVC来获取高并发性(默认级别为:Repeatable)

InnoDB体系结构|description
---|---
1|InnoDB有多个内存块,组成了一个大的内存池
2|多线程<br>Master Thread: 异步刷新数据到磁盘,保证数据的一致性<br>Purge Thread: 回收已经使用并分配的undo页
3|InnoDB存储引擎是基于磁盘存储的,并将记录按照页的方式进行管理
4|读取页<br>**从磁盘读取 → 放入缓冲池(FIX) → 下次读取先判断有无在缓冲池**
5|`对数据库的修改,先改缓冲池的页,然后再以一定频率刷新到磁盘上`
6|show engine innodb status查看INNODB状态
7|缓冲池是通过LRU进行管理的<br>当不能存放新读取到的页时,将先释放LRU表尾的页
8|当Update或Delete改变表中记录时,页是脏的<br>数据库需要将新版本的页从缓冲池刷新到磁盘
9|两种Checkpoint分为: Sharp Checkpoint 和 Fuzzy Checkpoint<br>sharp checkpoint：在关闭数据库的时候，将buffer pool中的脏页全部刷新到磁盘中<br>fuzzy checkpoint：数据库运行时，在不同的时机将部分脏页写入磁盘（刷新部分脏页到磁盘）<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;是为了避免一次刷新全部的脏页造成的性能问题。
10|
