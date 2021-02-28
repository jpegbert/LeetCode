"""
29. 两数相除

题目描述：
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2


示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2


提示：
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
"""


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    int_max = pow(2, 31)
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend > -int_max:
            # 只要不是最小的那个整数，都是直接返回相反数就好啦
            # 因为本题中的条件是数值范围是[-2^31,2^31-1]，所以当dividend=-2^31并且divisor=-1时是唯一一种溢出的情况
            return -dividend
        return int_max - 1 # 是最小的那个，那就返回最大的整数啦
    a = dividend
    b = divisor
    sign = 1
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        sign = -1
    a = abs(a)
    b = abs(b)
    res = div(a, b)
    if sign > 0:
        if res > int_max - 1:
            return int_max - 1
        else:
            return res
    return -res


def div(a, b):
    if a < b:
        return 0
    count = 1
    tb = b # 在后面的代码中不更新b
    """
    while tb + tb <= a:
        count = count + count # 最小解翻倍
        tb = tb + tb # 当前测试的值也翻倍
    """
    # 使用左移比上面那种直接相加的方式更快
    while tb << 1 <= a:
        count = count << 1 # 最小解翻倍
        tb = tb << 1 # 当前测试的值也翻倍

    """
    如果不用下面那句return时候的递归，使用这段也是可以的，只是这种方式比递归慢，会超时
    while tb <= a:
    count += 1
    tb += b
    """

    return count + div(a - tb, b)


def main():
    dividend = 10
    divisor = 3
    # dividend = 7
    # divisor = -1
    # dividend = -1
    # divisor = -1
    res = divide(dividend, divisor)
    print(res)


if __name__ == '__main__':
    main()
