# Pytest

* 需要按照下面的规则：
   * 测试文件以test_开头（以_test结尾也可以）
   * 测试类以Test开头，并且不能带有 init 方法
   * 测试函数以test_开头
   * 断言使用基本的assert即可

# 只测试某个方法
```
python -m pytest xxx.py::XXX(class)::xxx(def) -v
注意是用两个冒号隔开！
```

* 参数
   * -m
   ```
   @pytest.mark.xxx
   def abc():
   ```
   > "xxx" 执行xxx标记的test方法   
   > "not xxx" 执行没有xxx标记的test方法   
   * -v 每个测试函数执行结果
   * -q 只显示整体结果
   * -s 只显示print
   * -x 有一个出错就退出
   * -h 帮助
   * --cov
   ```
   需要下载pytest-cov检测覆盖率
   --cov=   覆盖率位置
   --cov-report=   报告类型
   --no-cov-on-fail   测试失败则不生成报告
   ```
