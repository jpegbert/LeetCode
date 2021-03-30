"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


def spiralOrder(matrix):
    """
    已AC
    :param matrix:
    :return:
    """
    res = []
    if matrix is None or len(matrix) == 0:
        return res
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1
    numEle = len(matrix[0]) * len(matrix)

    while numEle >= 1:
        for i in range(left, right + 1):
            if numEle >= 1:
                res.append(matrix[top][i])
                numEle -= 1
        top += 1
        for i in range(top, bottom + 1):
            if numEle >= 1:
                res.append(matrix[i][right])
                numEle -= 1
        right -= 1
        for i in range(right, left - 1, -1):
            if numEle >= 1:
                res.append(matrix[bottom][i])
                numEle -= 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if numEle >= 1:
                res.append(matrix[i][left])
                numEle -= 1
        left += 1
    return res


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    res = spiralOrder(matrix)
    print(res)


if __name__ == '__main__':
    main()
