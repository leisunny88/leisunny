"""ATM机允许4位或6位密码，而密码只能包含4位或6位数字。

如果函数传递了一个有效的PIN字符串，返回true，否则返回false。"""


def pass_password(password):
    pass


'''伪代码实现：给定只含0-9的数字字符串以及一个给定的整数，
通过二元操作符（+，-，*，/）操作字符串中的数字，可得到给定的整数值。
试列出所有的二元表达式。注意：单个表达式中，每个数字字符有且只能使用一次。'''


def gen_operator(d):  # 生成对应个数的操作符号组合列表
    res = []
    choice = ['+', '-', '*']
    t = [0] * d

    def loop(t, n):
        if n == d:
            c = t.copy()  # 可变
            res.append(c)
        else:
            for i in choice:
                t[n] = i
                loop(t, n + 1)

    loop(t, 0)
    return res


from itertools import combinations  # 这里使用内置函数，不再重复造轮子
import re


def addOperators(nums, target):
    res = []

    ex_nums = [' '] * (len(nums) * 2 - 1)  # 输入数字字符串扩展成列表。例如：['1', ' ', '2', ' ', '3']
    space_index = []
    for index, i in enumerate(nums):
        ex_nums[2 * index] = i
        space_index.append(2 * index + 1)
    space_index.pop()  # 得到对应的下标列表。例如：[1, 3]

    for i in range(1, len(space_index) + 1):
        """数字分割方式。例如：可以选下标1插入一个操作符（1？23），也可也选择下标3插入一个操作符（12？3），
        或者选择下标1和3插入两个操作符（1？2？3）。所以有i种情况。"""
        index_comb = combinations(space_index, i)  # 得到i个分割操作符的所有组合
        for index_tuple in index_comb:
            for operator_list in gen_operator(i):  # 生成i个操作符号的组合
                tmp = ex_nums.copy()  # 复制不改变原始列表
                for operator, index in zip(operator_list, index_tuple):
                    tmp[index] = operator  # 对应下标赋值
                setence = ''.join(["%s" % a for a in tmp if a != ' '])  # 生成字符串
                # 去掉‘1+05’这种操作符后面跟‘0’的情况，否则eval函数报错
                setence = re.sub(r'[\+\-\*]0+[1-9]+', lambda m: m.group().replace('0', ''), setence)
                if eval(setence) == target:  # eval转化成有效表达式求值并判断
                    res.append(setence)
    return res


# print(addOperators('123', 6))
# print(addOperators('105', 5))
# print(addOperators('00', 0))

import itertools
import re


# class Solution(object):
#     def addOperators(self, num, target):
#         if num:
#             count = len(num) - 1
#             rnum = num[-1]
#
#             s = "['','+','-','*'],"
#             ss = ""
#             for c in range(count):
#                 ss += s
#
#             ls = []
#             for item in itertools.product(*eval(ss[0:-1])):
#                 zty = ''.join(list(itertools.chain.from_iterable(zip(list(num), item)))) + rnum
#                 zty = re.sub(r'[\+\-\*]0+[1-9]+', lambda m: m.group().replace('0', ''), zty)
#                 if eval(zty) != target or re.match(r".*([\+\-\*]0)\d.*", zty, re.M | re.I):
#                     continue
#                 else:
#                     ls.append(zty)
#             return ls
#
#         return []

# print(Solution().addOperators("105", 5))


class Solution(object):
    def addOperators(self, s, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        n = len(s)
        ans = []
        if s == "":
            return []

        def solve(now, i, v, prev, last):
            if i == n:
                # if eval(now)!=v:
                #     print now,v
                if v == target:
                    ans.append(now)
                return
            # add
            solve(now + "+" + s[i], i + 1, v + int(s[i]), int(s[i]), int(s[i]))
            # sub
            solve(now + "-" + s[i], i + 1, v - int(s[i]), -int(s[i]), int(s[i]))
            # multi
            solve(now + "*" + s[i], i + 1, v - prev + prev * int(s[i]), prev * int(s[i]), int(s[i]))
            if s[i] != '0':
                solve(now + "/" + s[i], i + 1, v - prev + prev / int(s[i]), prev / int(s[i]), int(s[i]))
            # space
            if last != 0:
                solve(now + s[i], i + 1, v + 9 * prev + int(s[i]) * prev / last, 10 * prev + int(s[i]) * prev / last,
                      last * 10 + int(s[i]))

        solve(s[0], 1, int(s[0]), int(s[0]), 1)
        return ans


print(Solution().addOperators('105', 2))
