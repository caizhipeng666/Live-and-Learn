# Mysql

* [安装](#安装)

# 安装
> 解压安装包后，在主目录下创建data文件夹和my.ini配置文件
### 编辑ini配置文件
```
[client]
port=3306
default-character-set=utf8
[mysqld]
port=3306
character_set_server=utf8
basedir=xxx\mysql-5.7.25-winx64\
#解压目录
datadir=xxx\mysql-5.7.25-winx64\data
#解压目录下data目录
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
[WinMySQLAdmin]
xxx\mysql-5.7.25-winx64\bin\mysqld.exe
```
### 环境变量
```
输入变量名：MYSQL_HOME
输入变量值：xxx\MySql5.7\mysql-5.7.20-winx64

编辑：PATH
加入变量值：xxx\MySql5.7\mysql-5.7.20-winx64\bin
```
### 管理员打开cmd
```
mysqld --initialize
```
### 启动服务
```
net start mysql
```
### 找到密码
```
data\auto.cnf
```
> 没有密码存在的情况： 修改ini
```
[mysqld]
skip-grant-tables  # 添加
```
> 即可跳过登录，直接重设密码
### 运行mysql重设密码
```
mysql -u root -p

update user set authentication_string=password('新密码') where user="root";
flush priviledges;
```
