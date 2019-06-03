# 

* [pip](#pip)
* [pycurl](#pycurl)

# pip
### pip
```
python3.6 -m pip install -r requirements.txt --user
```
> 加速
```
-i https://mirrors.aliyun.com/pypi/simple/ 
```

# pycurl
### 错误1：
> ImportError: pycurl: libcurl link-time ssl backend (openssl) is different from compile-time ssl backend (none/other)
```
# pip uninstall pycurl
# export PYCURL_SSL_LIBRARY=openssl
# pip install pycurl
```

### 错误2：
> ImportError: pycurl: libcurl link-time ssl backend (nss) is different from compile-time ssl backend (openssl)
```
错误2的解决办法如下：
# pip uninstall pycurl
# export PYCURL_SSL_LIBRARY=nss
# pip install pycurl
```