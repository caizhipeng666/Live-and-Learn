# 常用小窍门

---
classify|
---|
[日期处理](#日期)|

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
