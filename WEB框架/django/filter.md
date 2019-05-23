* [filter](#filter)
* [select](#select)
* [others](#others)

# filter
```python
filter = {
'exact': '= %s',  
'iexact': 'LIKE %s',  
'contains': 'LIKE BINARY %s',  
'icontains': 'LIKE %s',  
'regex': 'REGEXP BINARY %s',  
'iregex': 'REGEXP %s',  
'gt': '> %s',   # grant than
'gte': '>= %s',  
'lt': '< %s',   # litte than
'lte': '<= %s',  
'startswith': 'LIKE BINARY %s',  
'endswith': 'LIKE BINARY %s',  
'istartswith': 'LIKE %s',  
'iendswith': 'LIKE %s'
}
```
---
# select
> 仅选某字段
```python
XX.objects.all().only('name')
```
> 去掉某字段
```python
XX.objects.all().defer('name')
```
---
# others
* 字段值为'\u...'
```python
# Ex：["\u4e60 \u54d2 \u54d2"]
# 使用print(["\u4e60 \u54d2 \u54d2"])可以直接看到结果
通过django, xxx.objects.filter(...).xx字段获取时:
      '["\\u4e60 \\u54d2 \\u54d2"]'
    通过json.loads()处理一下就OK
```
