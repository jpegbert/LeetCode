"""
题目描述：
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:
L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def convert1(s, numRows):
    res = []
    char_list = [[] for i in range(numRows)]
    curr_row = 0
    is_down = False
    for i in range(len(s)):
        if numRows == 1: # 针对输入字符串是两个字符，numRows是1的情景
            char_list[curr_row].append(s[i])
        else:
            char_list[curr_row].append(s[i])
            if (curr_row == 0) or (curr_row == numRows - 1):
                is_down = not is_down
            if is_down:
                curr_row += 1
            else:
                curr_row -= 1
    for i in range(len(char_list)):
        res.extend(char_list[i])
    return "".join(res)


def convert2(s, numRows): # 找规律
    pass


def main():
    s = "AB" # "LEETCODEISHIRING"
    res = convert1(s, 1)
    print(res)


if __name__ == '__main__':
    main()
