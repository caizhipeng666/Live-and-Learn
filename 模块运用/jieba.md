# 中文分组库 - jieba

1. 文本处理(可忽略)
```python
a = ' ,zxc 啊爱你 我'
a = a.strip().replace(' ', '')
```

2. 分词处理
```python
import jieba
b = jieba.cut(a, cut_all=False)
res = []
c = " ".join(b)  # cut后的对象
d = c.split(' ')  # 将分词用空格分隔
print(d)
```
* jieba.cut()
  * cut_all=True 全模式，返回所有可能分词
  * cut_all=False 精确模式，返回最大可能分词
