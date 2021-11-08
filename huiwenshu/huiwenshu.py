

def isPalindrome(x):
    x = str(x)
    start = 0
    end = len(x) - 1
    while start < end and x[start] == x[end]:
        start += 1
        end -= 1
    if start == end or ((start - 1 == end) and (x[start] == x[end])):
        return True
    else:
        return False


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1


def longestPalindrome(s):
    """
    AC ---- leetcode 第5题
    中心扩展法
    """
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
    num = 11
    res = isPalindrome(num)
    print(res)


if __name__ == '__main__':
    main()
