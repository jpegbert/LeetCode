"""
58. 最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。


示例 1：
输入：s = "Hello World"
输出：5

示例 2：
输入：s = " "
输出：0

提示：
1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
通过次数170,532提交次数496,857
"""


def lengthOfLastWord(s):
    """
    已AC
    :param s:
    :return:
    """
    word_list = s.split()
    if len(word_list) == 0:
        return 0
    else:
        return len(word_list[-1])


def main():
    s = "Hello World"
    s = " "
    res = lengthOfLastWord(s)
    print(res)


if __name__ == '__main__':
    main()
