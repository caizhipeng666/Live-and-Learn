# 数据库
---

数据库类型|
---|
[mysql](#mysql)|

```
SELECT TABLE_NAME AS '表名',
CONCAT(ROUND(TABLE_ROWS/10000, 2), ' 万行') AS '行数',
CONCAT(ROUND(DATA_LENGTH/(1024*1024*1024), 2), ' GB') AS '表空间',
CONCAT(ROUND(INDEX_LENGTH/(1024*1024*1024), 2), ' GB') AS '索引空间',
CONCAT(ROUND((DATA_LENGTH+INDEX_LENGTH)/(1024*1024*1024),2),' GB') AS'总空间'
FROM information_schema.TABLES WHERE TABLE_SCHEMA = '数据库名' ORDER BY TABLE_ROWS DESC;
```

# mysql
* [创建](#mysql创建)
* [查询](#mysql查询)
* [更新](#mysql更新)
* [替換](#mysql替換)
* [错误](#mysql错误)
* [索引](#mysql索引)
* [结构](#mysql结构)

错误码|说明
---|---
[1267](#1267)| 插入错误 (也有可能是django.db.utils.OperationalError: (1366, "Incorrect string value:))

## mysql创建
* 设置默认值为当前时间
```
default CURRENT_TIMESTAMP
```

## mysql查询
* 日期分组(日期排序)
```
select DATE(create_time), count(*), lecture_id
from xxx
where id > 1 and id < 10 and create_time > '2019-05-27'
GROUP BY lecture_id
ORDER BY DATE(create_time)
```
* 不使用cache
```
select sql_no_cache *
...
```

## mysql更新
1. 修改数据库级别
```
SET SQL_SAFE_UPDATES=0;
```
2. update字段
```
update xxx表
set 字段=值, 字段2=值2 (不是用AND连接!!!)
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
---
# mysql索引
## 强制使用索引
```
select *
from xx表 force index(索引名/主键)
```
## 强制不用索引
```
select *
from xx表 ignore index(索引名/主键)
```
---
# mysql结构
## 查看表
```
show tables from xxx_database;
```
## 查看列
```
show columns from xxx_table;
```
