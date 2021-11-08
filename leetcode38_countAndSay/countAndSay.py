
def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    if n <= 1:
        return "1"
    elif n == 2:
        return "11"
    elif n == 3:
        return "21"
    else:
        return countAndSay(n - 1)



def main():
    res = countAndSay(n)



if __name__ == '__main__':
    main()
