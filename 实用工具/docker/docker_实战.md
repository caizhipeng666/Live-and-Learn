# Docker实战
num|description
---|---
[1](#1)|build mysql


# 1
### build mysql
> Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
```
docker run --name czp_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7
```
