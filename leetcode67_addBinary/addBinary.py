"""
67. 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。


示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"

提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


def addBinary(a, b):
    """
    解法1：先把二进制转换为十进制，然后再把十进制转换为二进制 已AC
    :type a: str
    :type b: str
    :rtype: str
    """
    a = int(a, 2)
    b = int(b, 2)
    res = a + b
    return str(bin(res))[2:]


def addBinary1(a, b):
    """
    模拟 已AC
    :param a:
    :param b:
    :return:
    """
    res = []
    jinwei = 0
    n = max(len(a), len(b))
    for i in range(n):
        tmp_a = a[len(a) - 1 - i] if i < len(a) else 0
        tmp_b = b[len(b) - 1 - i] if i < len(b) else 0
        tmp_sum = int(tmp_a) + int(tmp_b)
        curr_val = (tmp_sum + jinwei) % 2
        jinwei = (tmp_sum + jinwei) // 2
        res.insert(0, str(curr_val))
    if jinwei > 0:
        res.insert(0, '1')
    return "".join(res)


def addBinary2(a, b):
    """
    移位
    把 a 和 b 转换成整型数字 x 和 y，在接下来的过程中，x 保存结果，y 保存进位。
    当进位不为 0 时
    - 计算当前 xx 和 yy 的无进位相加结果：answer = x ^ y
    - 计算当前 xx 和 yy 的进位：carry = (x & y) << 1
    - 完成本次循环，更新 x = answer，y = carry
    返回 x 的二进制形式
    """
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y # 无进位
        carry = (x & y) << 1 # 进位
        x, y = answer, carry # 更新
    return bin(x)[2:]


def main():
    a = "11"
    b = "1"
    res = addBinary2(a, b)
    print(res)


if __name__ == '__main__':
    main()
