# Sorted
---
> 内置的sorted()函数有一个关键字参数key，可传入一个callable对象给它   
> 这个callabel对象对每个传入的对象返回一个值，这个值被sorted()用来排序这些对象   
---
1. lambda 函数　
> 有一个User 实例序列，希望通过他们的user id 属性进行排序，可提供一个以User 实例作为输入并输出对应user id 值的callable 对象
```python
def sort_notcompare():
　　users = User.objects.filter(...)

　　print(sorted(users, key=lambda u: u.user.id))
```

2. operator.attrgetter()
> 另外一种方式是使用operator.attrgetter() 来代替lambda 函数：
```python
from operator import attrgetter

sorted(users, key=attrgetter('user_id'))
```
　　▲attrgetter() 函数通常会运行的快点，并且还能同时允许多个字段进行比较。
```python
如果User 实例还有一个first name 和last name 属性排序，

by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
```

3. min() 和max()
> 适用于像min() 和max() 之类的函数。
```python
from operator import attrgetter

min(users, key=attrgetter('user_id')
max(users, key=attrgetter('user_id')
```

4. 对复合数据使用
```python
s = [{'x': x, 'xxx':xxx}, {'x': xx, 'xxx':xxxx}]
s = sorted(s, key=lambda x: x['xxx'])
```
