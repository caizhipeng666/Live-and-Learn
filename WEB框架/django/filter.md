* [filter](#filter)
* [select](#select)

# filter
```python
filter = {
'exact': '= %s',  
'iexact': 'LIKE %s',  
'contains': 'LIKE BINARY %s',  
'icontains': 'LIKE %s',  
'regex': 'REGEXP BINARY %s',  
'iregex': 'REGEXP %s',  
'gt': '> %s',  
'gte': '>= %s',  
'lt': '< %s',  
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
