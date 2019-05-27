# 常用小窍门

---
classify|
---|
[去除转义](#去除转义)|
[类型检查](#类型检查)|
[日期处理](#日期)|
[字典处理](#字典)|
# 去除转义
```
string = r'xxxx\t\n'
```
# 类型检查
```
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
