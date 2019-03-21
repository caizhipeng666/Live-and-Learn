# coding=utf-8
"""
请实现一个函数，
将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
"""


# 第一种解法
def replace(before):
    if not before:
        return False
    after = before.replace(' ', '%20')
    return after


# 第二种解法
def replace2(before):
    if not before:
        return False
    after = ''
    for s in before:
        after += s if s != ' ' else '%20'
    return after


# 第三种解法
def replace3(before):
    if not before:
        return False
    before = list(before)
    after = ''
    for s in before:
        if s == ' ':
            s = '%20'
        after += s
    return after


# 单元测试
import unittest


class TestReplace(unittest.TestCase):

    before = '123 as d'
    after = '123%20as%20d'

    def setUp(self):
        print('开始测试')

    def tearDown(self):
        print('测试结束')

    def test_replace1(self):
        self.assertEqual(self.after, replace(self.before))

    def test_replace2(self):
        self.assertEqual(self.after, replace2(self.before))

    def test_replace3(self):
        self.assertEqual(self.after, replace3(self.before))

    def test_error(self):
        self.assertEqual(False, replace(''))


if __name__ == '__main__':
    unittest.main()