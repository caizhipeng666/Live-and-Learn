# Linux命令

命令|说明
---|---
[mkdir](#mkdir)|创建文件夹
[curl](#curl)|Ping URL
[wget](#wget)|Download URL
[> xxx.txt](#输出文件)|输出文件
[ps](#ps)|进程信息
[grep](#grep)|查找信息

---
# mkdir
* -p:当上级目论不存在时，创建上级目录
---
# curl
* curl [option] [url]

参数|作用
---|---
-x|使用代理，Ex:curl -x xxx.ip:80 http:xx.com
-A|模拟浏览器，EX:curl -A "Mozilla/4.0..." http:xx.com
-e|伪造refer

---
# wget
> 下载文件的工具

---
# 输出文件
> 将控制台输出，添加到文件中
```
python xxx.py > ~/xxx/xx.txt
```
---
# ps
参数|作用
---|---
-e|显示所有进程
-f|全格式
-ef|显示所有进程所有内容

UID|PID|PPID|C|STIME|TTY|TIME|CMD
---|---|---|---|---|---|---|---
拥有者|程序ID|父级ID|CPU资源占比|系统启动时间|登录者ip|使用掉的CPU|时间|下达的指令

> 通常与grep一起使用，Ex:ps -ef | grep python

---
# grep
参数|作用
---|---
-i|忽略大小写
-v|反转匹配
-w|精准匹配
-n|显示行号
-m num|只匹配num条
