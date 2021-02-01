"""
有效的括号

题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

示例 4：
输入：s = "([)]"
输出：false

示例 5：
输入：s = "{[]}"
输出：true
 
提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

链接：https://leetcode-cn.com/problems/valid-parentheses
"""


def isMatch(last_kuohao, curr_kuohao):
    if (last_kuohao == "(" and curr_kuohao == ")") or (last_kuohao == "{" and curr_kuohao == "}") or (last_kuohao == "[" and curr_kuohao == "]"):
        return True
    else:
        return False


def isValid(s):
    """
    自己的解法，已AC
    :type s: str
    :rtype: bool
    """
    if len(s) % 2 == 1:
        return False
    history_kuohao_list = []
    for i in range(len(s)):
        curr_kuohao = s[i]
        if len(history_kuohao_list) == 0:
            history_kuohao_list.append(curr_kuohao)
        else:
            last_kuohao = history_kuohao_list[-1]
            is_match = isMatch(last_kuohao, curr_kuohao)
            if is_match:
                del history_kuohao_list[-1]
            else:
                history_kuohao_list.append(curr_kuohao)
    if len(history_kuohao_list) == 0:
        return True
    else:
        return False


def isValid1(s):
    """
    官方解法
    :param s:
    :return:
    """
    if len(s) % 2 == 1:
        return False
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def main():
    s = "()" # True
    s = "()[]{}" # True
    s = "(]" # False
    s = "([)]" # False
    s = "{[]}" # True
    res = isValid(s)
    print(res)


if __name__ == '__main__':
    main()
