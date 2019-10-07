# TOX 自动化项目
> Command line driven CI frontend and development task automation tool   
> https://github.com/tox-dev/tox   

### 能够在同一个Host上自定义出多套相互独立且隔离的python环境
> pip install tox

## tox command
command|description
---|---
tox -e pep8|对代码进行检查
[tox -e py27](#py27)|构建测试环境

### py27
1. tox会读取项目根目录下的tox.ini
2. 根据该文件来构建出相应的虚拟环境
3. 将该虚拟环境保存在.tox/目录下的相应文件中

## tox.ini
```
[tox]
envlist = py27,py37
skipsdist = True
indexserver =
toxworkdir={toxinidir}/../var/.tox
default = https://pypi.doubanio.com/simple

# 默认集成方案
[testenv]
changedir = {toxinidir}/.. 
deps = pytest
setenv = 
    xxx = xx
    PYTHONPATH = {toxinidir}/py27
commands = pytest

# 需要使用tox -e czp
[testenv:czp]
install_command = pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com {opts} {packages}
deps = -r{toxinidir}/requirements.txt
commands = {posargs:py.test}
```
---
> https://tox.readthedocs.io/en/latest/config.html

key|description
---|---
envlist|在哪些环境下进行发布、安装、测试相关
skipsdis|=True时tox默认会使用sdist构建包，(没有必要)，而且构建还会要求存在README、setup.py等文件
toxworkdir|创建virtual虚拟环境的路径
changedir|执行命令时更改，以该目录当前目录
deps|包测试依赖
setenv|导入变量，跟export一样
commands|测试命令
