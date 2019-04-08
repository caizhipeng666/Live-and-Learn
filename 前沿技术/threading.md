# Threading
module|说明
---|---
[构建类](#class)|threading.Thread()
[运行](#start)|.start()
[等待](#join)|.join()

---
attribute
* [名称](#name)
* [存活](#is_alive())
* [守护](#daemon)

---
more|说明
---|---
[索对象](#lock对象)|threading.Lock()

# class
```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```
> 构造函数传入的参数都是关键字参数
* group:永远是None, 留待未来扩展功能
* target:应该是可调用的对象,后续会被run()方法调用,默认为None
* name:指定线程的名字,默认会指定Thread-N的名字形式
* args:传入一个元组或iterable,取出每个元素作为target的参数
* kwargs:传入一个字典,取出键值对作为target的关键字参数
* daemon:如果指定,那就会显性的设定是否为守护线程,如果为None,则从创建他的线程中继承

# start
### 每个thread 对象都只能被调用1次start()
> 启动线程, 最多只能调用一次(因为run()方法执行后会删除对象的target属性和args属性),由他来调用对象的run()方法
```python
def test(x):
    print(x)

t = threading.Thread(target=test, name='test', args=(5,), daemon=True)
t.start()
print(t.is_alive())
```
* args须为iterable
> 所以此处为(5,） 而不能是5或者(5)

# join
> join(timeout=None)等待直到线程终止   
> * 正常   
> * 非正常终止   
> * 发生超时   
>> 通过调用is_alive方法来判断它是否发生超时
```python
def loop(nloop,nsec):
    print('开始循环',nloop,'at:',ctime())
    sleep(nsec)
    print('循环',nloop,'结束于：',ctime())

loops = [1,2,3]
threads = []
nloops = range(len(loops))

for i in nloops:
    t = threading.Thread(target=loop, args=(i, loops[i]))  # 循环实例化3个Thread类,将线程对象放入一个列表中
    threads[i].start()  # 循环开始线程
    threads.append(t)

for t in threads:
    t.join()  # 循环join()让主线程等待所有线程执行完毕。
```


# name
```python
t = threading.Thread()
t.name = 'xxx'
print(t.name)
```
# is_alive()
```python
t = threading.Thread()
t.start()
print(t.is_alive())
```
# daemon
> A boolean value indicating whether this thread is a daemon thread (True) or not (False). This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False   
> The entire Python program exits when no alive non-daemon threads are left
```python
t = threading.Thread()
t.daemon = True
print(t.daemon)

# 老方法(遗弃)
t.setDaemon(True)
```

---
# lock对象
> acquire()和release()   
---
1. acquire
> acquire(blocking=True, timeout=-1)
* blocking为Ture:一直阻塞直到锁设置为unlock状态,然后立即返回True并把锁设为lock状态
* blocking为False:不会被阻塞,返回值会有差异;当在lock状态下时返回False,其他状态下将锁设为lock状态并返回True
2. release
> 释放lock;可在任何线程中调用(不局限于获取锁的线程)
---


# Demo
```python
import threading


class XXThread(threading.Thread):
    def __init__(self):
        super().__init__()  #(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
        self.xx = 'xx'

    def run(self):
        print('XXThread: {}'.format(self.xx))


x = XXThread()
x.start()
print(x)
```

✗高级嵌套
```python
class ThreadManager(object):
    def __init__(self):
        self.threads = []

    def thread_func(self):
        t = XXThread(...)
        t.start()
        self.threads.append(t)
    def thread_join(self, timeout=60):
        for t in slef.threads:
            t.join(timeout)
        return ...

class XXThread(threading.Thread):
    ...
```
