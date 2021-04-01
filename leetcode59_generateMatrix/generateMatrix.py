"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。


示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]

提示：
1 <= n <= 20
"""


def generateMatrix(n):
    """
    自己根据前面一个螺旋矩阵的解题思路写的，已AC
    :type n: int
    :rtype: List[List[int]]
    """
    res = [[0] * n for i in range(n)]
    left, right, top, bottom = 0, n - 1, 0, n - 1
    curr_val = 1
    while curr_val <= n * n:
        # 上面从左到右
        for i in range(left, right + 1):
            res[top][i] = curr_val
            curr_val += 1
        top += 1
        # 右侧从上到下
        for i in range(top, bottom + 1):
            res[i][right] = curr_val
            curr_val += 1
        right -= 1
        # 下方从右到左
        for i in range(right, left - 1, -1):
            res[bottom][i] = curr_val
            curr_val += 1
        bottom -= 1
        # 左侧从下到上
        for i in range(bottom, top - 1, -1):
            res[i][left] = curr_val
            curr_val += 1
        left += 1
    return res


def generateMatrix(n):
    """
    官方解法,已AC
    :param n:
    :return:
    """
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        for row in range(top + 1, bottom + 1):
            matrix[row][right] = num
            num += 1
        if left < right and top < bottom:
            for col in range(right - 1, left, -1):
                matrix[bottom][col] = num
                num += 1
            for row in range(bottom, top, -1):
                matrix[row][left] = num
                num += 1
        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return matrix


def main():
    n = 3
    n = 1
    res = generateMatrix(n)
    print(res)


if __name__ == '__main__':
    main()
