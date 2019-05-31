# 高级ORM用法
* [Annotate](#Annotate)
* [Case](#Case)
* [When](#When)
---

# Annotate
> Group By
```python
# 通过group_by "x1_id", "x2_id"进行数据库去重
reviewer = queryset.values('x1_id', 'x2_id').annotate(Count('x2_id'))
```
### Annotate高级使用
> 将DateTimeField的日期，进行每一天的Group_by
```python
from django.db.models.functions import TruncDay

tasks_annotate = queryset.annotate(
        day=TruncDay('start_time')
    ).values('day').annotate(
        tasks_count=Count('id')
    ).values('day', 'tasks_count').order_by('day')
# 第一个annotate:聚合成每一天
# 第二个annotate:根据每一天进行Group By
```

# 数据模型
```python
from django.db import models

class Client(models.Model):
    REGULAR = 'R'
    GOLD = 'G'
    PLATINUM = 'P'
    ACCOUNT_TYPE_CHOICES = (
        (REGULAR, 'Regular'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    )
    name = models.CharField(max_length=50)
    registered_on = models.DateField()
    account_type = models.CharField(
        max_length=1,
        choices=ACCOUNT_TYPE_CHOICES,
        default=REGULAR,
    )
```

# Case
> 将部分数据到新的列
### xxx = Case()
1. 添加测试数据
```python
from datetime import date, timedelta
from django.db.models import CharField, Case, Value, When
Client.objects.create(
    name='Jane Doe',
    account_type=Client.REGULAR,
    registered_on=date.today() - timedelta(days=36))
Client.objects.create(
    name='James Smith',
    account_type=Client.GOLD,
    registered_on=date.today() - timedelta(days=5))
Client.objects.create(
    name='Jack Black',
    account_type=Client.PLATINUM,
    registered_on=date.today() - timedelta(days=10 * 365))
# Get the discount for each Client based on the account type
```
2. 实现
```python
Client.objects.annotate(
    discount=Case(
        When(account_type=Client.GOLD, then=Value('5%')),
        When(account_type=Client.PLATINUM, then=Value('10%')),
        default=Value('0%'),
        output_field=CharField(),
     ),
).values_list('name', 'discount')
```
> [('Jane Doe', '0%'), ('James Smith', '5%'), ('Jack Black', '10%')]

# When
> 输出聚合数据
1. 添加测试数据
```python
Client.objects.create(
    name='Jean Grey',
    account_type=Client.REGULAR,
    registered_on=date.today())
Client.objects.create(
    name='James Bond',
    account_type=Client.PLATINUM,
    registered_on=date.today())
Client.objects.create(
    name='Jane Porter',
    account_type=Client.PLATINUM,
    registered_on=date.today())
```
2. 实现
```python
Client.objects.aggregate(
    regular=Sum(
        Case(When(account_type=Client.REGULAR, then=1),
             output_field=IntegerField())
    ),
    gold=Sum(
        Case(When(account_type=Client.GOLD, then=1),
             output_field=IntegerField())
    ),
    platinum=Sum(
        Case(When(account_type=Client.PLATINUM, then=1),
             output_field=IntegerField())
    )
)
```
