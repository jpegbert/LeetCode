"""
实现 strStr()

题目描述：
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:
输入: haystack = "hello", needle = "ll"
输出: 2

示例 2:
输入: haystack = "aaaaa", needle = "bba"
输出: -1

说明:
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""


def strStr(haystack, needle):
    """
    方法1：自己的解法，已AC
    :param haystack:
    :param needle:
    :return:
    """
    if len(needle) == 0:
        return 0
    i, j = 0, 0
    while i < len(haystack) and j < len(needle):
        if needle[j] == haystack[i]:
            if j == len(needle) - 1:
                return i - j
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    return -1


def strStr1(haystack, needle):
    """
    方法2：官方解法，子串逐一比较 - 线性时间复杂度
    :param haystack:
    :param needle:
    :return:
    """
    m, n = len(haystack), len(needle)
    for i in range(m - n + 1):
        if haystack[i: i + n] == needle:
            return i
    return -1


def strStr2(haystack, needle):
    """
    方法3：官方解法，双指针 - 线性时间复杂度
    :param haystack:
    :param needle:
    :return:
    """
    L, n = len(needle), len(haystack)
    if L == 0:
        return 0

    pn = 0
    while pn < n - L + 1:
        while pn < n - L + 1 and haystack[pn] != needle[0]:
            pn += 1

        # compute the max match string
        curr_len = pL = 0
        while pL < L and pn < n and haystack[pn] == needle[pL]:
            pn += 1
            pL += 1
            curr_len += 1

        # if the whole needle string is found,
        # return its start position
        if curr_len == L:
            return pn - L

        # otherwise, backtrack
        pn = pn - curr_len + 1

    return -1


def strStr(haystack, needle):
    """
    方法3：官方解法 Rabin Karp - 常数复杂度
    :param haystack:
    :param needle:
    :return:
    """
    L, n = len(needle), len(haystack)
    if L > n:
        return -1

    # base value for the rolling hash function
    a = 26
    # modulus value for the rolling hash function to avoid overflow
    modulus = 2 ** 31

    # lambda-function to convert character to integer
    h_to_int = lambda i: ord(haystack[i]) - ord('a')
    needle_to_int = lambda i: ord(needle[i]) - ord('a')

    # compute the hash of strings haystack[:L], needle[:L]
    h = ref_h = 0
    for i in range(L):
        h = (h * a + h_to_int(i)) % modulus
        ref_h = (ref_h * a + needle_to_int(i)) % modulus
    if h == ref_h:
        return 0

    # const value to be used often : a**L % modulus
    aL = pow(a, L, modulus)
    for start in range(1, n - L + 1):
        # compute rolling hash in O(1) time
        h = (h * a - h_to_int(start - 1) * aL + h_to_int(start + L - 1)) % modulus
        if h == ref_h:
            return start


def main():
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    haystack = ""
    needle = "a"
    haystack = ""
    needle = ""
    res = strStr(haystack, needle)
    print(res)


if __name__ == '__main__':
    main()
