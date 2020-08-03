
"""
无重复字符的最长子串

题目描述：
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
"""
"""
思路：双指针法，后指针向后移一个位置，此时要循环判断该位置的元素是否在前后指针截取的字符串中，若存在，需要不断向后移动前一个指针，直到当前位置的元素不在两个指针截取的字符串中；若当前位置元素不在前后指针截取的字符串中，需要记录当前最大长度，并与全局最大长度比较，此外后指针右移一位
"""


def lengthOfLongestSubstring(s):
    max_len = 0
    tmp_max_len = 0
    start = 0
    end = 0
    while end != len(s):
        tmp_s = s[start:end]
        while s[end] in tmp_s:
            start += 1
            tmp_max_len -= 1
            tmp_s = s[start:end]
        tmp_max_len += 1
        if max_len < tmp_max_len:
            max_len = tmp_max_len
        end += 1
    return max_len


def main():
    res = lengthOfLongestSubstring("abab")
    print(res)


if __name__ == '__main__':
    main()
