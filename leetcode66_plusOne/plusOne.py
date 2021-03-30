"""
66. 加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。


示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

提示：
1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


def plusOne(digits):
    """
    自我解法，已AC
    :param digits:
    :return:
    """
    n = len(digits)
    jinwei = 0
    result = []
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            curr = digits[i] + 1 + jinwei
        else:
            curr = digits[i] + jinwei
        curr_val = curr % 10
        jinwei = curr // 10
        result.insert(0, curr_val)
    while jinwei != 0:
        curr_val = jinwei % 10
        result.insert(0, curr_val)
        jinwei = jinwei // 10
    return result


def main():
    digits = [1, 2, 3]
    digits = [4, 3, 2, 1]
    digits = [0]
    digits = [999]
    res = plusOne(digits)
    print(res)


if __name__ == '__main__':
    main()
