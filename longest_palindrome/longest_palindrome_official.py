"""
最长回文子串

题目描述：
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

题解：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/
"""


def longestPalindrome1(s): # 动态规划法
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    ans = ""
    # 枚举子串的长度 l+1
    for l in range(n):
        # 枚举子串的起始位置i，这样可以通过 j=i+l 得到子串的结束位置
        for i in range(n):
            j = i + l
            if j >= len(s):
                break
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j + 1]
    return ans


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


def longestPalindrome2(s): # 中心扩展法
    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = expandAroundCenter(s, i, i)
        left2, right2 = expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end + 1]


def main():
    res = longestPalindrome1("ac") # 动态规划
    res = longestPalindrome2("ac") # 中心扩展法
    # Manacher 算法，比较复杂
    print(res)


if __name__ == '__main__':
    main()
