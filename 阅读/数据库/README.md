# ✦重要

classify|
---|
[mysql](#mysql)|

---
# mysql
* [sql执行顺序](#mysql执行顺序)

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
```
4. where
5. group by
6. avg,sum...(聚合函数)
7. having
8. select
9. distinct
10. order by
