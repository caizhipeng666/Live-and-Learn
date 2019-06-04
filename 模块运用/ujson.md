# Ujson
> 速度比json快一倍,但是安装很麻烦！

1. dumps
```python
ujson.dumps("czp nb")
```
* 参数：
    * ensure_ascii(Boolean)
    * encode_html_chars(Boolean)
    * double_precision(int) 保留几位小数
    * escape_forward_slashes(Boolean) False时去除转义
2. loads
```python
ujson.loads("czp nb")
```
