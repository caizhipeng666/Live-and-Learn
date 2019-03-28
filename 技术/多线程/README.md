Threading

module|
---|
[构建类](#class)|
[运行](#start)|
[等待](#join)

---
attribute|
---|
[名称](#name)|
[存活](#is_alive())|
[守护](#daemon)|


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

# join(timeout=None)
> 等待直到线程终止   
> * 正常   
> * 非正常终止   
> * 发生超时   
>> 通过调用is_alive方法来判断它是否发生超时
```python

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
