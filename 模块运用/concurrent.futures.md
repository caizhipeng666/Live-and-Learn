# concurrent.futures

classicfy|description
---|---
[Executor](#Executor)|ThreadPoolExecutor/ProcessPoolExecutor
[Future](#Future)|有Executor.submit产生多任务

# Executor
### THreadPoolExecutor
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    print(list(executor.map(sleeper, x)))
```
### ProcessPoolExecutor
```python
def xxx():
with ProcessPoolExecutor(max_workers=2) as executor:
        return {num:factors for num, factors in
                                zip(nums,
                                    executor.map(factorize_naive, nums))}
```

# Future
```python

```
objects|description|return
---|---|---
Future.cancel()|终止某个线程和进程的任务|Boolean
Future.cancelled()|判断是否结束了任务|Boolean
Future.running()|判断是否还在运行|Boolean
Future.done()|判断是正常执行完毕|Boolean
Future.result(timeout=None)|针对result结果做超时的控制|

---
> ✘不要在已经被submit的函数里面在调用submit
> 
