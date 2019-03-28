Threading

module|
---|
[构建类](#class)|


# class
```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```
> 构造函数传入的参数都是关键字参数
* group参数永远是None, 留待未来扩展功能
* target参数应该是可调用的对象,后续会被run()方法调用,默认为None
* name参数指定线程的名字,默认会指定Thread-N的名字形式
* args参数传入一个元组或iterable,取出每个元素作为target的参数
* kwargs参数传入一个字典,取出键值对作为target的关键字参数
* daemon参数如果指定,那就会显性的设定是否为守护线程,如果为None,则从创建他的线程中继承

