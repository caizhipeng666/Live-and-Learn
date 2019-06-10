# HTTPIE
> https://pypi.org/project/httpie/

function|
---|
[Get](#Get)|
[Post](#Post)|
[Print](#Print)|
---
### 如果键值对用: ☛ 头部
### ⚛HTTP 方法的名称在 URL 参数之前

# Get
```python
http ip:port/xxx/api/ param1==x1 parma2==x2
```
### 本地Get
```python
http :/xxx
```

# Post
```python
http httpbin.org/post  --  param1=x1
```
### 表单
```python
http --form POST xxx.com/xx/1 name='Czp'
```

# Print
> --print, -p
```python
字符 	代表
H 	请求头
B 	请求体
h 	响应头
b 	响应体

http --print=Hh PUT xxx.com/put hello=world
```
