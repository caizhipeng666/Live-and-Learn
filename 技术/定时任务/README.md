# APScheduler
---
说明|使用
---|---
[定义](#定义)|介绍
[控制器](#控制器)| Scheduler()
[作业存储](#作业存储)|job stores
https://www.cnblogs.com/quijote/p/4385774.html
https://www.cnblogs.com/luxiaojun/p/6567132.html
https://apscheduler.readthedocs.io/en/latest/userguide.html
---

# 定义
### 官方介绍
> Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs it should have run while it was offline
### 组成
* scheduler 控制器
* job stores 作业存储   
   (1)默认的作业存储是把作业保存在内存中，(可以设置为保存在数据库中)。   
   (2)一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。   
   (3)🔺调度器不能分享同一个作业存储   
* executors 执行者
> 处理作业的运行，在一个线程或者进程池来进行，当作业完成时，执行器将会通知调度器
* triggers 触发器
> 按日期、按时间间隔、按cronjob描述式三种触发方式   
* schedulers 调度

# 控制器
### 种类
* BlockingScheduler: use when the scheduler is the only thing running in your process
> 调用start函数后会阻塞当前线程
* BackgroundScheduler: use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
> 调用start后主线程不会阻塞
* AsyncIOScheduler: use if your application uses the asyncio module
* GeventScheduler: use if your application uses gevent
* TornadoScheduler: use if you’re building a Tornado application
* TwistedScheduler: use if you’re building a Twisted application
* QtScheduler: use if you’re building a Qt application
### 实例化
```python
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()
```

# 作业存储
### job stores
```python
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

# scheduler维护自己的executor和jobstore表
jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
# 多进程实现(每个job在运行时，是通过一个进程池来作为worker实际执行的，这个进程池最大size是20)
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```
---
> job_defaults参数定义了一些特殊行为：
    coalesce：当由于某种原因导致某个job积攒了好几次没有实际运行（比如说系统挂了5分钟后恢复，有一个任务是每分钟跑一次的，按道理说这5分钟内本来是“计划”运行5次的，但实际没有执行），如果coalesce为True，下次这个job被submit给executor时，只会执行1次，也就是最后这次，如果为False，那么会执行5次（不一定，因为还有其他条件，看后面misfire_grace_time的解释）   
    max_instance: 就是说同一个job同一时间最多有几个实例再跑，比如一个耗时10分钟的job，被指定每分钟运行1次，如果我们max_instance值为5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了   
    misfire_grace_time：设想和上述coalesce类似的场景，如果一个job本来14:00有一次执行，但是由于某种原因没有被调度上，现在14:01了，这个14:00的运行实例被提交时，会检查它预订运行的时间和当下时间的差值（这里是1分钟），大于我们设置的30秒限制，那么这个运行实例不会被执行。   

> 每隔5s的任务
* scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
> 12s后
* scheduler.add_job(func=aps_test, args=('一次性任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
> 每3s
* scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3)
##### ▲调用start函数后，job()并不会立即开始执行。而是等待3s后，才会被调度执行
