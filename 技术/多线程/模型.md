```python
import threading


class XXThread(threading.Thread):
    def __init__(self):
        super().__init__()  #(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
        self.xx = 'xx'

    def run(self):
        print('XXThread: {}'.format(self.xx))


x = XXThread()
x.start()
print(x)
```

✗高级嵌套
```python
class ThreadManager(object):
    def __init__(self):
        self.threads = []

    def thread_func(self):
        t = XXThread(...)
        t.start()
        self.threads.append(t)
    def thread_join(self, timeout=60):
        for t in slef.threads:
            t.join(timeout)
        return ...

class XXThread(threading.Thread):
    ...
```
