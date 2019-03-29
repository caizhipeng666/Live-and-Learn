# Mock
> 请求拦截 
---
* [Responses](#Responses)
* [Pook](#Pook)
---
# Responses
```python
import responses

def mock_test():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as resp:
        # 同样使用add()方法定义
        resp.add(resp.GET,  # 可用resp.add_callback(...)
                 'https://xxx/xxx',  # 可用re.compile(r'http.+/xxxx/.*')正则匹配url
                 json={
                     'xxx': 'xxxxxxxx',
                     'personal': {
                         'DOB': '6/29/1991',
                         'Ht': '67',
                         'Wt': '230'
                     }},
                 status=200,
                 content_type='application/json'
                 )
# 使用
@mock_test
class XXX:
```
> assert_all_requests_are_fired=False来避免AssertionError: Not all requests have been executed
---
> 如果使用resp.add_callback()
```python
def request_callback(request):
        resp_body = json.loads(request.body)  # 如果需要处理body
        headers = {'xxx': 'xxx'}
        return (200, headers, json.dumps(resp_body))
# 使用
responses.add_callback(
        responses.GET, 'http://xxx.com/xxx',
        callback=request_callback,
        content_type='application/json',
    )
```
> 当callback的函数有多个参数时,可以使用partial偏函数来减轻函数
```python
def callback函数(request, xxx):
    pass
responses.add_callback(
        responses.POST, re.compile(r'http.+/xxxx/.*'),
        partial(callback函数, 参数='xxx')
    )
```


# Pook
```python
import pook

@pook.get('http://xxx/500', reply=204, json={...})
@pook.get('http://xxx/400', reply=200)
def fetch(url):
    return requests.get(url)
    
res = fetch('http://xxx/400')
res = fetch('http://xxx/500')
print('status:', res.status_code)
```
