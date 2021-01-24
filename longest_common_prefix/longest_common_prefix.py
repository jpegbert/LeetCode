
"""
最长公共前缀
题目描述：
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

链接：https://leetcode-cn.com/problems/longest-common-prefix
"""


def longestCommonPrefix(strs):
    if len(strs) <= 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_len = min([len(l) for l in strs])
    i = 1
    flag = True
    while i < min_len + 1:
        sub_str = strs[0][:i]
        for j in range(1, len(strs)):
            tmp = strs[j][:i]
            if sub_str != tmp:
                flag = False
                break
        if flag is False:
            break
        i += 1
    return strs[0][: i - 1]


def main():
    # strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    # strs = ["a"]
    strs = ["ab", "a"]
    res = longestCommonPrefix(strs)
    print("--", res)


if __name__ == '__main__':
    main()
