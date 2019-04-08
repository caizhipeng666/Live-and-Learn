# Docker坑

* [ubuntu](#ubuntu)

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
