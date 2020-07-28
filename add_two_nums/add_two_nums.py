
"""
题目描述
输入两个整数，求这两个整数的和是多少。

输入格式
输入两个整数A,B，用空格隔开，0≤A,B≤108
输出格式
输出一个整数，表示这两个数的和

样例输入：
3 4

样例输出：
7
"""


def add(a, b):
    while b != 0:
        tmp_a = a ^ b # 不带进位的加法
        tmp_b = (a & b) << 1 # 进位值
        a = tmp_a
        b = tmp_b
    return a


def main():
    a = 999
    b = 1
    print(add(a, b))


if __name__ == '__main__':
    main()
