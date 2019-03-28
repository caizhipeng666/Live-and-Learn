# Threading多线程

## **Czp**   
---

# 官方介绍
> This module constructs higher-level threading interfaces on top of the lower level _thread module   
> * See also the queue module    

> 该模块在较低级别thread模块之上构建更高级别的线程接口。另请参见mutex和Queue模块   
### Note
---
>   While they are not listed below, the camelCase names used for some methods and functions in this module in the Python 2.x series are still supported by this module

>   从Python 2.6开始，该模块提供 符合 PEP 8的别名和属性，以替换camelCase受Java的线程API启发的名称   
>   此更新的API与multiprocessing模块的API兼容   
>   但是，没有为camelCase名称的弃用设置计划，它们在Python 2.x和3.x中仍然完全受支持

---
CPython实现细节：
> 在CPython中，由于全局解释器锁定，只有一个线程可以一次执行Python代码   
>（即使某些面向性能的库可能会克服此限制）  
* ∴如果应用程序更好地利用多核机器的计算资源，建议使用multiprocessing
* 但是，如果要同时运行多个I / O限制任务，线程仍然是一个合适的模型

---
Classify |
--- | 
[官方文档](https://docs.python.org/3/library/threading.html "官方文档") |
[中文文档](https://cloud.tencent.com/developer/section/1371311 "中文网") |
[实现示例](https://blog.csdn.net/Mr_Slower/article/details/83958758 "示例") |

---
