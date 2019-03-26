# APScheduler
---
说明|使用
---|---
[定义](#定义)|介绍
[控制器](#控制器)| Scheduler()
[作业存储](#作业存储)|job stores
[任务调度](#任务调度)|executor
[触发器](#触发器)|trigger
[监听](#监听)|日志
[Example](#Example)|实战

---

# 定义
### 官方介绍
> Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. You can add new jobs or remove old ones on the fly as you please. If you store your jobs in a database, they will also survive scheduler restarts and maintain their state. When the scheduler is restarted, it will then run all the jobs it should have run while it was offline
### 组成
* scheduler 控制器
* job stores 作业存储   
   * 默认的作业存储是把作业保存在内存中，(可以设置为保存在数据库中)。   
   * 一个作业的数据讲在保存在持久化作业存储时被序列化，并在加载时被反序列化。   
   * 🔺调度器不能分享同一个作业存储   
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
> scheduler维护自己的executor和jobstore表
### 种类
* MemoryJobStore：没有序列化，jobs就存在内存里，增删改查也都是在内存中操作
* SQLAlchemyJobStore：所有sqlalchemy支持的数据库都可以做为backend，增删改查操作转化为对应backend的sql语句
* MongoDBJobStore：用mongodb作backend
* RedisJobStore: 用redis作backend
### 实例化
```python
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
# jobstore提供给scheduler一个序列化jobs的统一抽象，提供对scheduler中job的增删改查接口
```

# 任务调度
> 每个job在运行时，是通过一个进程池来作为worker实际执行的
### 种类
   * threadpool
   * processpoll
### 实例化
```python
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
```

```python
job_defaults = {
    'coalesce': False,
    'max_instances': 3,
    'misfire_grace_time': 30
}
```
```python
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```
> 暂停作业:
```python
apsched.job.Job.pause()  # scheduler.pause()
apsched.schedulers.base.BaseScheduler.pause_job()  # scheduler.pause_job('my_job_id')
```
> 恢复作业:
```python
apsched.job.Job.resume()  
apsched.schedulers.base.BaseScheduler.resume_job()
```
> 默认情况下调度器会等待所有正在运行的作业完成后，关闭所有的调度器和作业存储。如果你不想等待，可以将wait选项设置为False。
```python
scheduler.shutdown()
scheduler.shutdown(wait=False)
```

job_defaults参数定义了一些特殊行为:   
* 1. 某个job积攒了好几次没有实际运行(如系统挂了5分钟)   
  * 'coalesce': True/False
    * coalesce为True，下次这个job被submit给executor时，只会执行1次，即最后的那次,
    * coalesce为False，那么会执行5次（不一定，因为还有其他条件，看后面misfire_grace_time的解释）
* 2. 设定同一个job同一时间最多有几个实例再跑   
  * max_instance: 5
    * 如一个耗时10分钟的job，每分钟运行1次,
    * 如果max_instance值为5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了
* 3. 某个job的定时任务没有调度   
  * 'misfire_grace_time': 30
    * 一个job在14:00有一次执行，但是没有被调度上，现在14:01了,
    * 这个14:00的运行实例被提交时，会检查它预订运行的时间和当下时间的差值(现在14:01差了1分钟),
    * 大于了设置的30秒限制，∴实例不会被执行

# 触发器
### 种类
    > 一个任务何时被触发
   * 日期(date,最少用)
   * interval(时间间隔)
   * cron(与unix crontab格式兼容,最为强大)
### 实例化
> 每隔5s的任务
```python
* scheduler.add_job(func=xxx, args=('定时任务(参数1)',), trigger='cron', second='*/5')
```
> 12s后
```python
* scheduler.add_job(func=xxx, args=('一次性任务(参数1)', '(参数2)'), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
```
> 每3s
```python
* scheduler.add_job(func=xxx, args=('循环任务(参数1)',), trigger='interval', seconds=3)
```
> 2017年3月22日17时19分07秒执行
```python
sched.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)
```
> 在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00执行
```python
sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
```
> 从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
```python
sched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')
```

# 监听
>  当job抛出异常时，APScheduler会默默的把他吞掉，不提供任何提示
### 种类
* job – the job instance in question
* scheduled_run_time – the time when the job was scheduled to be run
* retval – the return value of the successfully executed job
* exception – the exception raised by the job
* traceback – the traceback object associated with the exception
### ∴我们必须知晓程序的任何差错。→注册listener，可以监听一些事件
* job抛出异常
* job没有来得及执行
```python
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

def my_listener(event):
    err_logger = logging.getLogger('schedErrJob')
    if event.exception:
        err_logger.exception('%s error.', str(ev.job))
    else:
        err_logger.info('%s miss', str(ev.job))

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
```
### 如果需要查看详细日志
```python
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
scheduler._logger = logging
scheduler.start()
```
### ❌需要动态引入一次依赖包logging(import logging)

# Example
```python
import time
from apscheduler.schedulers.blocking import BlockingScheduler
 
def my_job():
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
 
sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=5)
sched.start()

sched.remove_job('my_job_id')
```
##### ▲调用start函数后，job()并不会立即开始执行。而是等待3s后，才会被调度执行
##### ▲当job不以daemon模式运行时，并且APScheduler也不是daemon的，那么在关闭脚本时，Ctrl + C是不奏效的，必须kill才可以
