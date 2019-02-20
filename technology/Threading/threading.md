# Threading多线程

## **Czp**   
---

# 官方介绍
> This module constructs higher-level threading interfaces on top of the lower level _thread module. See also the queue module.
> 该模块在较低级别thread模块之上构建更高级别的线程接口。另请参见mutex和Queue模块
### Note
---
>   While they are not listed below, the camelCase names used for some methods and functions in this module in the Python 2.x series are still supported by this module

---
>   从Python 2.6开始，该模块提供 符合 PEP 8的别名和属性，以替换camelCase受Java的线程API启发的名称。此更新的API与multiprocessing模块的API兼容 。但是，没有为camelCase名称的弃用设置计划，它们在Python 2.x和3.x中仍然完全受支持

---
方法 | 说明
--- | ---
[threading.active_count()](#active_count()) | <span style="color: #A52A2A">返回正在运行的线程对象的数量</span>
[threading.current_thread()](#current_thread()) | <span style="color: #A52A2A">返回当前的线程对象</span>

---
# active_count()
#### 返回正在运行的线程对象的数量,效果等同于计算enumerate()列表的长度
>   Return the number of Thread objects currently alive. The returned count is equal to the length of the list returned by enumerate()


```python
import threading
import time


def test1(x):
    print('test1-->{}'.format(x))
    time.sleep(3)
    print('test1 end')


def test2(x):
    print('test2-->{}'.format(x))
    time.sleep(5)
    print('test2 end{}'.format(x + 1))


a = threading.Thread(target=test1, args=(5,))  # args必须iterable
b = threading.Thread(target=test2, args=(6,))
a.start()
b.start()
print(threading.active_count())
a.join()
print('ending')
print(threading.active_count())
```

---
# current_thread()
#### 返回当前的线程对象,即是代码调用者的控制线程, 如果调用者的控制线程不是在threading模块中创建的, 那返回的将是一个被限制功能的线程对象
>   Return the current Thread object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the threading module, a dummy thread object with limited functionality is returned

```python
def test1(x): 
    print('test1-->{}'.format(x)) 
    time.sleep(3)
    print('test1 end') 
    print(threading.current_thread()) 
a = threading.Thread(target=test1, args=(5,)) 
a.start() 
print(threading.current_thread())
```

