# map
---
> map(func, *iterables) --> map object 
---
1. 自定义函数
```python
def xx(x):
    print('xxx')
    return x+1
list = [...]
map(xx, list)
```
2. 匿名函数
```python
list = [...]
map(lambda x: x+1, list)
```

# 重中之重！
> ⚝python3的map与python2的map不同   
> python3的只是一个迭代器！   
```python
# 真正需要迭代使用时:
list(map(xx, list))
```