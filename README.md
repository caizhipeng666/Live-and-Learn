# Live-and-Learn
> It's never too late to learn
---
# By czp
* 2019-05-20 Mysql where order by limit
1. xx表中，time有索引
```
select *
from xx
where id = 1
and time = '2019-05-20'
order by time
limit 10
```
```
select *
from xx
where id = 2
and time = '2019-05-20'
order by time
limit 10
```
> 效率极其低下，其中1比2要慢很多
### 疑惑
* 索引用了time，为什么不用id？
> 实际上用索引id大多数情况还是要比用索引time要快
```

```
* 两个字段都有索引，为什么不能一起使用？
```
数据的指针，如果用一个索引来查询，其原理就是从索引树上去检索，并获得这些指针，然后去取出数据，
试想，如果你通过一个索引，得到过滤后的指针，
这时，你的另一个条件索引如果再过滤一遍，将得到2组指针的集合，
如果这时候取交集，未必就很快，
因为如果每个集合都很大的话，取交集的时候，等于扫描2个集合，效率会很低，所以没法用2个索引。
当然有时候mysql会考虑临时建立一个联合索引，将2个索引联合起来用，
但是并不是每种情况都能奏效，
同样的道理，用一个索引检索出结果集之后，排序时，也无法用上另一个索引了。
```
### 原因:
* ⚑当有order by 和 limit同时存在时，查询的顺序就有可能发生变化   
   这时并不是从数据库中先通过where过滤再排序再limit   
* 数据库先根据time索引树，从最左侧叶子节点(asc)，取出n条，然后逐条去跟where条件匹配   
  若匹配上，则得出一条数据，直至取满10条为止   
  为什么第二条sql要快，因为运气好，刚好时间倒序的前几条就全部满足了。
### 解决
✓ 组合索引(但是要注意组合索引的顺序, id_time 和 time_id效果是不同的)
* 可能会出现的问题：排序用到了filesort，也就是说，排序未用到索引   
  wher id in (1, 2, 3)
```
本来索引是排好序的，直接左序遍历即可，如 WHERE id = 4 order by time
4+time1
4+time2
4+time3
但是现在，下索引的排序规则
id1<id2<id3...  time1<time2<time3....
查询结果集排序如下：
id1+time1
id1+time2
id1+time3

id2+time1
id2+time2
id2+time3
id是有序的，时间是无序的，因为有多个id，优先按id排序，时间就是乱的了
∴排序将会用filesort
```
```
MySQL5.7文档中有一节——8.2.1.16 LIMIT Query Optimization，里面有这样一句话：
If an index is not used for ORDER BY but a LIMIT clause is also present, 
the optimizer may be able to avoid using a merge file 
and sort the rows in memory using an in-memory filesort operation. 
For details, see The In-Memory filesort Algorithm.
在ORDER BY + LIMIT的查询语句中，如果ORDER BY不能使用索引的话，优化器可能会使用in-memory sort操作。
详情请参考https://dev.mysql.com/doc/refman/5.7/en/order-by-optimization.html#order-by-filesort-in-memory
```
✓ 改为子查询
```
优化前的SQL需要更多I/O浪费
因为先读索引,再读数据,然后抛弃无需的行,
而优化后的子查询,只读索引(Cover index)就可以了
```
