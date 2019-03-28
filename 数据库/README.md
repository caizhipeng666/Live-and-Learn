# 数据库
---

数据库类型|
---|
[mysql](#mysql)|


# mysql
* [更新](#mysql更新)
* [替換](#mysql替換)

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

## mysql替換
```
update xxx表
set xx字段=replace(xx字段,'匹配xxx','替换xxxx')
where ...;
```
> ▲两个xx字段要相同

