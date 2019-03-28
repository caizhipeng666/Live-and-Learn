# 高级用法
* [外部修改配置](#override_settings)
---


# override_settings
> 在settings外修改django配置
```python
from django.test import override_settings

@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                                       'LOCATION': 'unique-snowflake'}})
```