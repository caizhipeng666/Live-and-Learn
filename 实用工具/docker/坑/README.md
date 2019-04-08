# Docker坑

* [时区](#时区)
* [ubuntu](#ubuntu)

# 时区
```
export TZ=Asia/Shanghai
```

# ubuntu
```
docker run -d -p 80:80 --name webserver nginx
```
> http://localhost   
> 就能访问nginx了   
```
docker run -it ubuntu bash
```
> apt-get install git 出现错误 : Unable to locate package
```
apt-get update
```
