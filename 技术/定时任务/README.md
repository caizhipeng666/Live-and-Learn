# APScheduler
---
说明|使用
---|---
[定义](#定义)|介绍
[控制器](#控制器)| Scheduler()
[定义](#定义)|介绍

---

# 定义
### 官方介绍
> Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs it should have run while it was offline
### 组成
* scheduler 控制器
* job stores 工作存储
> 存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。调度器不能分享同一个作业存储
* executors 执行者
* triggers 触发器
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
> 每隔5s的任务
* scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
> 12s后
* scheduler.add_job(func=aps_test, args=('一次性任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
> 每3s
* scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3)
##### ▲调用start函数后，job()并不会立即开始执行。而是等待3s后，才会被调度执行
