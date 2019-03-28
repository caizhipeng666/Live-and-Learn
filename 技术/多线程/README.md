Threading

module|
---|
[构建类](#class)|
[运行](#start)|


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
def test1(x):
    print('test1-->{}'.format(x))
    time.sleep(3)
    print('test1 end'

t = threading.Thread(target=test1, name='fuck', args=(5,6,7), daemon=True)  # args须为iterable
t.start()
```
