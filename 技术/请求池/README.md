# requests_toolbelt

This module provides three classes:
* Pool
* ThreadResponse
* ThreadException
---
```python
import queue
from requests_toolbelt.threaded import pool

jobs = queue.Queue()
urls = [
    # My list of URLs to get
]

for url in urls:
    queue.put({'method': 'GET', 'url': url})

p = pool.Pool(job_queue=q)
p.join_all()

for response in p.responses():
    print('GET {0}. Returned {1}.'.format(response.request_kwargs['url'],
                                          response.status_code))
```