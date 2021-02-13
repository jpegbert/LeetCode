"""
括号的生成

题目描述：
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

示例 2：
输入：n = 1
输出：["()"]

提示：
1 <= n <= 8

链接：https://leetcode-cn.com/problems/generate-parentheses
"""


def generate(A, n, ans):
    if len(A) == 2 * n:
        if valid(A):
            ans.append("".join(A))
    else:
        A.append('(')
        generate(A, n, ans)
        A.pop()
        A.append(')')
        generate(A, n, ans)
        A.pop()


def valid(A):
    bal = 0
    for c in A:
        if c == '(':
            bal += 1
        else:
            bal -= 1
        if bal < 0:
            return False
    return bal == 0


def generateParenthesis(n):
    """
    官方解法1
    时间复杂度：O(2^(2n) * n) 其中 2^(2n) 是序列长度，n是检验
    空间复杂度O(n)
    :type n: int
    :rtype: List[str]
    """
    ans = []
    generate([], n, ans)
    return ans


def backtrack(S, left, right, ans, n):
    if len(S) == 2 * n:
        ans.append(''.join(S))
        return
    if left < n:
        S.append('(')
        backtrack(S, left + 1, right, ans, n)
        S.pop()
    if right < left:
        S.append(')')
        backtrack(S, left, right + 1, ans, n)
        S.pop()


def generateParenthesis1(n):
    """
    官方解法2 回溯法提前判断状态
    :param n:
    :return:
    """
    ans = []
    backtrack([], 0, 0, ans, n)
    return ans


def get_parenthesis(curr, left, right, ans):
    if left == 0 and right == 0:
        ans.append(curr)
        return
    if left >= right: # 左括号的数量比右括号的数量多，只能加右括号
        get_parenthesis(curr + "(", left - 1, right, ans)
    else: # left < right # 右括号的数量比左括号的数量多，左右括号都可以加
        if left > 0:
            get_parenthesis(curr + "(", left - 1, right, ans)
        get_parenthesis(curr + ")", left, right - 1, ans)


def generateParenthesis2(n):
    """
    leetcode上别人的解法
    :param n:
    :return:
    """
    ans = []
    if n <= 0:
        return ans
    get_parenthesis("", n, n, ans)
    return ans


def main():
    n = 3
    res = generateParenthesis2(n)
    # print("".join(res))
    print(res) # ['((()))', '(()())', '(())()', '()(())', '()()()']


if __name__ == '__main__':
    main()
