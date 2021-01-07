"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321
 
示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def reverse(x):
    if x >= 0:
        reversed_x = int(str(x)[::-1])
    else:
        reversed_x = -int(str(x)[:0:-1])

    if -2 ** 31 < reversed_x < 2 ** 31 - 1:
        return reversed_x
    else:
        return 0


def reverse1(x):
    if x is None:
        return
    res = 0
    while x != 0:
        pop = x % 10
        res = res * 10 + pop
        # 这里是判断不能超过整数的范围，需要判断，但是测试没通过
        # import sys
        # if res > sys.maxsize or res < (-sys.maxsize - 1):
        if res <= -2 ** 31 or res >= 2 ** 31 - 1:
            return 0
        x = int(x / 10)
    return int(res)


def main():
    x = 1563
    res = reverse1(x) # 字符翻转
    print(res)


if __name__ == '__main__':
    main()
