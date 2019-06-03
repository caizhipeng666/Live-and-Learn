# concurrent.futures

classicfy|description
---|---
[Executor](#Executor)|ThreadPoolExecutor/ProcessPoolExecutor
[Future](#Future)|有Executor.submit产生多任务

# Executor
1. 选择池
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
2. 安排计划
### sumbit(fn, *args, **kwargs)
> Schedules the callable, fn, to be executed as fn(*args **kwargs)   
> returns a Future object representing the execution of the callable   
```
with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 323, 1235)
    print(future.result())
```
### map(func, *iterables, timeout=None, chunksize=1)
### shutdown(wait=True)

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
