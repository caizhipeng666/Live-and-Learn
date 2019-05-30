# Linux

命令|说明
---|---
[mkdir](#mkdir)|创建文件夹
[curl](#curl)|Ping URL
[wget](#wget)|Get URL
[> xxx.txt](#>txt)|输出文件
[ps](#ps)|进程信息
[grep](#grep)|查找信息

---
# mkdir
* -p:当上级目论不存在时，创建上级目录
---
# curl
---
# wget
---
# >txt
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
拥有者|程序ID|父级ID|CPU使用的资源百分比|系统启动时间|登入者的终端机位置|使用掉的CPU|时间|下达的指令

> 通常与grep一起使用，Ex:ps -ef|grep python
---
# grep
