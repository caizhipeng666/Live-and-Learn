# 常用小窍门

---
classify|
---|
[git](#git)|
[去除转义](#去除转义)|
[类型检查](#类型检查)|
[日期处理](#日期)|
[字典处理](#字典)|
[集合操作](#集合)|
# git
```
git branch | grep -v "master" | xargs git branch -D
git stash && git checkout master && git branch | grep -v "master" | xargs git branch -D
```
# 去除转义
```python
string = r'xxxx\t\n'
```
# 类型检查
```python
def xx(xxx: int):
```
# 日期
   > import datetime
* 当前日期
```python
datetime.date.today()
```
* 当前时间(精确到秒)
```python
datetime.datetime.now()
```
* 加一天/减一天(hours小时 minutes分钟)
```python
datetime.timedelta(days=1)   # +1
datetime.timedelta(days=-1)  # -1
```

# 字典
   > 取出value相同的key
```python
some_dict = {'1': '1', '2': '2', '3': '1'}

new_dict = {}
for k, v in some_dict.items():
    new_dict.setdefault(v, []).append(k)

print(new_dict)
```

# 集合
```python
a = ['a', 'b', 'c', 1, 2]
b = ['b', 2]
c = ['c', 2]
d = set(filter(lambda x: x in a, b))  # d → {'b', 2}
e = set(filter(lambda x: x in a, c))  # e → {'c', 2}
```
action|description
---|---
&|交
\||并
^|异或
-|差
+|和
