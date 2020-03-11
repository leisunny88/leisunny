"""实现一个将两个数字相加并以二进制形式返回它们的和的函数。
转换可以在添加之前完成，也可以在添加之后完成。

返回的二进制数应该是一个字符串。"""


def add_binary(a, b):
    _sum = a + b
    res = bin(_sum)
    print(res[2:])
    return res[2:]


add_binary(51, 12)
