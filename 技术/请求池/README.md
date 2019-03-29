# requests_toolbelt

This module provides three classes:
* Pool
* ThreadResponse
* ThreadException
---
```python
import queue
from requests_toolbelt.threaded import pool

urls = [
    # My list of URLs to get
]

p = pool.Pool.from_urls(urls, , request_kwargs=dict(method='POST/GET/HEAD'))
# 也可以用下面的笨方法
jobs = queue.Queue()
for url in urls:
    queue.put({'method': 'GET', 'url': url})

p = pool.Pool(job_queue=q)
p.join_all()

for response in p.responses():
    print('GET {0}. Returned {1}.'.format(response.request_kwargs['url'],
                                          response.status_code))
```
* p.responses()     (status_code)
* p.exceptions()    (message)

The Pool object takes 4 other keyword arguments:
* initializer
* auth_generator
* num_processes
* session

