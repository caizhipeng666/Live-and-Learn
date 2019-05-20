# Mock.patch
> mock某个具体function 
---
* 接口
* 直接调用（探究）
---

# 接口
```python
@patch('xx文件夹下.xxPY文件.xxCLASS或者方法')
def test_xxx(mock_func):
    mock_func.return_value = ...
```
# 直接调用（探究）
```python
def mock_xxx(原先那个方法的参数...):
    return mock的返回值

@pytest.mark.asyncio
async def test_xxx():
  with patch('xx文件夹下.xxPY文件.xxCLASS或者方法', mock_xxx):
```
