# 常用小窍门

---
classify|
---|
[日期处理](#日期)|
[字典处理](#字典)|

# 日期
   > import datetime
* 当前日期
```
datetime.date.today()
```
* 当前时间(精确到秒)
```
datetime.datetime.now()
```
* 加一天/减一天(hours小时 minutes分钟)
```
datetime.timedelta(days=1)   # +1
datetime.timedelta(days=-1)  # -1
```

# 字典
   > 取出value相同的key
```
some_dict = {'1': '1', '2': '2', '3': '1'}

new_dict = {}
for k, v in some_dict.items():
    new_dict.setdefault(v, []).append(k)

print(new_dict)
```
