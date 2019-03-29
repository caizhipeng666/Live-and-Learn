# requests_toolbelt
* [Pool](#Pool)
* [Threaded](#Threaded)

This module provides three classes:
* Pool
* ThreadResponse
* ThreadException
---
> The Pool object takes 4 other keyword arguments:
> * initializer
> * auth_generator
> * num_processes
> * session
---
# Pool
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

---

# Threaded
> (也是Pool Object,所以也有4个属性)
```python
from requests_toolbelt import user_agent

def initialize_session(session):
    session.headers['User-Agent'] = user_agent('my-scraper', '0.1')
    session.headers['Accept'] = 'application/json'

urls_to_get = [{
    'url': 'https://api.github.com/repos/requests/toolbelt',
    'method': 'GET',
}, {
    'url': 'https://google.com',
    'method': 'GET',
}, ...]

responses, errors = threaded.map(urls_to_get, num_processes=10,
                                 initializer=initialize_session)
```
