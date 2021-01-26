"""
整数转罗马数字

题目描述：
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.


思路：一共就900, 400, 90, 40, 9, 4 这几个是比较特殊的，把这几个硬写出来。所有数据按照从大到小的顺序循环找
链接：https://leetcode-cn.com/problems/integer-to-roman
"""


def intToRoman(num):
    """
    方法1: 已AC
    :param num:
    :return:
    """
    res = ""
    trans_dict = {"1000": "M", "900": "CM", "500": "D", "400": "CD", "100": "C", "90": "XC", "50": "L", "40": "XL", "10": "X", "9": "IX", "5": "V", "4": "IV", "1": "I"}
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    while num != 0:
        for i in range(len(num_list)):
            curr_num = num_list[i]
            if num >= curr_num:
                res += trans_dict[str(curr_num)]
                num -= curr_num
    return res


def intToRoman1(num):
    """
    官方解法，已AC
    :param num:
    :return:
    """
    roman_digits = []
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
              (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    for value, symbol in digits:
        if num == 0: break
        # 下面这句与下面两句等效
        # count, num = divmod(num, value)
        count = num // value
        num = num % value
        print(count, num, symbol, value)
        roman_digits.append(symbol * count)
    return "".join(roman_digits)


def intToRoman3(num):
    """
    方法3: 已AC
    :param num:
    :return:
    """
    trans_dict = {"1000": "M", "900": "CM", "500": "D", "400": "CD", "100": "C", "90": "XC", "50": "L", "40": "XL", "10": "X", "9": "IX", "5": "V", "4": "IV", "1": "I"}
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_digits = []
    for i in range(len(num_list)):
        curr_num = num_list[i]
        if num >= curr_num:
            count = num // curr_num
            num = num % curr_num
            roman_digits.append(trans_dict[str(curr_num)] * count)
    return "".join(roman_digits)


def main():
    num = 671 # DCLXXI
    num = 3 # III
    num = 4 # IV
    num = 9 # IX
    num = 58 # LVIII
    num = 1994 # MCMXCIV
    res = intToRoman(num)
    # res = intToRoman1(num)
    print(res)


if __name__ == '__main__':
    main()
