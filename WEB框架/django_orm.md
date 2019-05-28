* [filter](#filter)
* [update](#update)
* [select](#select)
* [atomic](#atomic)

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
> 只要某字段
```python
XX.objects.all().only('name')
```
> 去掉某字段
```python
XX.objects.all().defer('name')
```
---
# atomic
1. context_manager
```python
with transaction.atomic():
    qs = XX.objects.select_for_update().filter(...)
```
2. decorate
```
@transaction.atomic
```
