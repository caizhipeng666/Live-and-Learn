# concurrent.futures

classicfy|description
---|---
[Executor](#Executor)|ThreadPoolExecutor/ProcessPoolExecutor
[Future](#Future)|用Executor.submit/map产生多任务
[Module](#Module)|模块方法
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
executor.shutdown()
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
> 如果不是获取到所有结果再处理，通常会使用 Executor.submit + Executor.as_completed
### map(func, *iterables, timeout=None, chunksize=1)
> 这个函数返回结果的顺序于调用开始的顺序是一致的
> submit方法能处理不同的可调用对象和参数，而map只能处理参数不同的同一个可调用对象
### shutdown(wait=True)
> if you use the with statement, which will shutdown the Executor
---
# Future
objects|description|return
---|---|---
Future.cancel()|终止某个线程和进程的任务|Boolean
Future.cancelled()|判断是否结束了任务|Boolean
Future.running()|判断是否还在运行|Boolean
Future.done()|判断是正常执行完毕|Boolean
Future.result(timeout=None)|针对result结果做超时的控制|
Future.add_done_callback(callable)|Future运行结束后会回调这个对象|

---
> ✘不要在已经被submit的函数里面在调用submit
---
# Module
function|description
---|---
ALL_COMPLETED|The function will return when all futures finish or are cancelled
FIRST_COMPLETED|The function will return when any future finishes or is cancelled.
FIRST_EXCEPTION|The function will return when any future finishes by raising an exception.  If no future raises an exception then it is equivalent to ALL_COMPLETED.

# Example
```python
import concurrent.futures

lists = [消耗队列]
def xxfunc(l: list):
    ...
    return

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    xx = {executor.submit(xxfunc, l): l for l in lists}
    # xx2 = dict((executor.submit(xxfunc, l), l) for l in lists)

    # 如果需要func的返回结果
    for future in concurrent.futures.as_completed(xx):
        # as_completed 接收一个future列表，返回值是一个迭代器
        xxx = xx[future]
        try:
            # func中的return
            data = future.result()
        except Exception as exc:
            print('exc', exc)
        else:
            pass
```
---
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as e:
    # map的parma2必须是个可迭代对象
    p = e.map(czp_test, range(5))
    print(list(p))
```
