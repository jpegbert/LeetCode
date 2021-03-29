"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。


示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

提示：
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""


def quickMul(x, N):
    if N == 0:
        return 1.0
    y = quickMul(x, N // 2)
    return y * y if N % 2 == 0 else y * y * x


def myPow(x, n):
    """
    官方解法
    :param x:
    :param n:
    :return:
    """
    return quickMul(x, n) if n >= 0 else 1.0 / quickMul(x, -n)


def myPow1(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    m = -n if n < 0 else n
    p, q = 1, x
    while m > 0:
        if (m & 1) == 1:
            p *= q
        m //= 2
        q *= q

    return 1 / p if n < 0 else p


def myPow2(x, n):
    """
    这种方式在理论上可行，实际上在本地python环境中会出现递归深度超出限制的情况，可是在leetcode中运行通过
    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n > 0:
        return power(x, n)
    else:
        return 1.0 / power(x, -1 * n)


def power(x, n):
    if n == 0:
        return 1

    a = power(x, n / 2)
    if n % 2 == 0:
        return a * a
    else:
        return a * a * x


def main():
    x = 2.00000
    n = 10
    # x = 2
    # n = -2
    res = myPow2(x, n)
    print(res)


if __name__ == '__main__':
    main()
