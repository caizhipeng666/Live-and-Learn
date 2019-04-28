# 数据库
---

数据库类型|
---|
[mysql](#mysql)|


# mysql
* [创建](#mysql创建)
* [更新](#mysql更新)
* [替換](#mysql替換)
* [错误](#mysql错误)

错误码|说明
---|---
[1267](#1267)| 插入错误 (也有可能是django.db.utils.OperationalError: (1366, "Incorrect string value:))

## mysql创建
* 设置默认值为当前时间
```
default CURRENT_TIMESTAMP
```
## mysql更新
1. 修改数据库级别
```
SET SQL_SAFE_UPDATES=0;
```
2. update字段
```
update xxx表
set 字段=值
where 字段=条件;
```
> 减少一天 set xx_time = DATE_SUB(expired_time,INTERVAL 1 DAY)

## mysql替換
```
update xxx表
set xx字段=replace(xx字段,'匹配xxx','替换xxxx')
where ...;
```
> ▲两个xx字段要相同

---
# mysql错误
## 1267
> 插入数据库错误：1267错误
```
ALTER TABLE xxx表 CONVERT TO CHARACTER SET utf8;
```
