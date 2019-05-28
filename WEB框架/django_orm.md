* [filter](#filter)
* [update](#update)
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
# update
1. 直接filer后update
```python
XX.ojects.filter(...).update()
```
2. 对queryset进行updae
```python
qs = XX.objects.filter(...)
qs = qs.exclude(...)[:3]
qs.update()
```
3. ✘对单个记录进行update(行不通的)
```python
qs = XX.objects.filter(...)
for q in qs:
    q.update(...) 报错：XX has no attribute 'update'
```
4. 使用save进行update
```python
qs = XX.objects.filter(...)
for q in qs:
    q.id = XX
    q.name = czp
    # q.save()可以使用update_fields提速
    q.save(update_fields=['id', 'name'])
```
---
# select
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
