

def my_atoi1(s):
    sign = 1  # 正负号标记
    base = 0  # 转换值
    i = 0  # 索引位
    exist_sign = False
    sign_list = ["+", "-"]
    while i < len(s) and s[i] == " ":  # 找到第一个非空字符
        i += 1
    while i < len(s) and s[i] in sign_list:
        if exist_sign:
            return 0
        exist_sign = True
        if s[i] == "+":
            sign = 1
        if s[i] == "-":
            sign = -1
        i += 1
    # 此时到了有效数字开始位置
    while i < len(s) and s[i].isnumeric():
        base = 10 * base + int(s[i])
        i += 1
    # 计算结果值
    res = base * sign
    minimum = -pow(2, 31)
    maxmum = pow(2, 31) - 1
    if res < minimum:
        return minimum
    elif res > maxmum:
        return maxmum
    else:
        return base * sign


def main():
    data = "+"
    res = my_atoi1(data)
    print(res)


if __name__ == '__main__':
    main()
