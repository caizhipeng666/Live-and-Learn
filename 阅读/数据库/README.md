# ✦重要

classify|
---|
[mysql](#mysql)|

---
# mysql
* [sql执行顺序](#mysql执行顺序)
* [sql表连接](#mysql表连接)

### mysql执行顺序
select * limit xx
1. from
```
    对from的前两个表形成笛卡儿积, ✓选择相对小的表作为基础表
```
2. join
3. on
```
    先判断on: 将on中的逻辑表达式应用到基础表的各行，筛选出满足on的各行 →→→ 生成新表
    生成新表: 通过join类型过滤
             1.left join on x.id = xx.id
             2.right join on
             3.outer join
```
4. where
```
    where是所有on筛选后的下一步筛选
```
5. group by(某个唯一字段/下面的聚合函数)
6. avg,sum...(聚合函数)
```
    将唯一的值合成为一组,结果集中：每个组只有一行
```
7. having
8. select
9. distinct
10. order by


### mysql表连接
1. left join
* 观察区别(and / where)
```
SELECT * 
FROM xx1 
     LEFT JOIN xx2 ON (xx1.id = xx2.id)
     AND xx2.id=2;
```
> 除了xx2.id=2的行有数据,其余行都为null →→→ 因为不符合on筛选
```
SELECT * 
FROM xx1 
     LEFT JOIN xx2 ON (xx1.id = xx2.id)
     Where xx2.id=2;
```
> 只筛选出了xx2.id=2的行
