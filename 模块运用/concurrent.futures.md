# concurrent.futures

classicfy|description
---|---
[Executor](#Executor)|ThreadPoolExecutor/ProcessPoolExecutor
[Future](#Future)|有Executor.submit产生多任务
[Example](#Example)|demo

# Executor
>  提供了执行异步调用，但不能直接使用
1. 选择池
### ThreadPoolExecutor
##### ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    print(list(executor.map(sleeper, x)))
```
```python
executor = ThreadPoolExecutor(max_workers=1)
executor.submit(xxxfunc, param1, ...)
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
> if you use the with statement, which will shutdown the Executor


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

# Example
```python
import concurrent.futures

lists = [消耗队列]
def xxfunc(l: list):
    ...
    return

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    xx = {executor.submit(xxfun, l): l for l in lists}
    for future in concurrent.futures.as_completed(xx):
        xxx = xx[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (xxx, exc))
        else:
            print('%r page is %d bytes' % (xxx, len(data)))
```
