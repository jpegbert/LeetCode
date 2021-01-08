

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


def main():
    num = 11
    res = isPalindrome(num)
    print(res)


if __name__ == '__main__':
    main()
