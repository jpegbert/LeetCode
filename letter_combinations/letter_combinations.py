"""
电话号码的字母组合

题目描述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

思路：
1、回溯法
2、常规解法
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""



def letterCombinations(digits):
    """
    自己的解法，已AC
    :type digits: str
    :rtype: List[str]
    """
    if not digits:
        return list()
    data_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    for i in range(len(digits)):
        first_str = data_dict[digits[i]]
        if i == 0:
            for char in first_str:
                res.append(char)
        else:
            tmp = []
            for char in first_str:
                for j in range(len(res)):
                    tmp.append(res[j] + char)
            res = tmp
    return res


def letterCombinations1(digits):
    """
    官方解法：回溯法
    :param digits:
    :return:
    """
    if not digits:
        return list()

    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(index):
        if index == len(digits):
            combinations.append("".join(combination))
        else:
            digit = digits[index]
            for letter in phoneMap[digit]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()

    combination = list()
    combinations = list()
    backtrack(0)
    return combinations


def main():
    digits = "23" # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    res = letterCombinations(digits)
    print(res)


if __name__ == '__main__':
    main()
