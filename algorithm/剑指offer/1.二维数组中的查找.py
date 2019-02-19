# coding=utf-8
"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def findnumber(target, array):
    if not array:
        return False
    if not target:
        return False
    # -1是为了计算下标
    rows = len(array) - 1
    columns = len(array[0]) -1
    i = 0
    while i <= rows and columns >= 0:
        if target == array[i][columns]:
            return True
        elif target > array[i][columns]:
            i += 1
        elif target < array[i][columns]:
            columns -= 1
    return False


# 单元测试部分
import unittest


class TestFindNumber(unittest.TestCase):
    """测试二维数组中的查找"""

    # 测试用例
    array1 = [[1, 6, 7], [9, 10, 15], [22, 37, 49]]
    array2 = []

    def tearDown(self):
        print('测试结束')

    def setUp(self):
        print('测试开始')

    def test_FindNumber_success(self):

        self.assertEqual(True, findnumber(10, self.array1))

    def test_FindNumber_error_null(self):
        self.assertEqual(False, findnumber(10, self.array2))

    def test_FindNumber_error_number(self):
        self.assertEqual(False, findnumber(11, self.array1))


if __name__ == '__main__':
    unittest.main()