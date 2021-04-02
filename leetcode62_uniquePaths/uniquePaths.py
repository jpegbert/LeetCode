"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

示例 1：
输入：m = 3, n = 7
输出：28

示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

示例 3：
输入：m = 7, n = 3
输出：28

示例 4：
输入：m = 3, n = 3
输出：6

提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
"""


res = 0


def uniquePaths(m, n):
    """
    自己的解法，各种case验证都可以通过，提交后超时
    :type m: int
    :type n: int
    :rtype: int
    """
    helper(0, 0, m, n)
    return res


def helper(row, col, m, n):
    global res
    if row == m - 1 and col == n - 1:
        res += 1
    if row + 1 < m:
        helper(row + 1, col, m, n)
    if col + 1 < n:
        helper(row, col + 1, m, n)


def uniquePaths1(m, n):
    """
    官方解法，已AC
    我们用 f(i, j) 表示从左上角走到 (i, j) 的路径数量，其中 i 和 j 的范围分别是 [0, m) 和 [0, n)。
    由于我们每一步只能从向下或者向右移动一步，因此要想走到 (i,j)，如果向下走一步，那么会从 (i-1, j) 走过来；
    如果向右走一步，那么会从 (i, j-1) 走过来。因此我们可以写出动态规划转移方程：
    f(i, j) = f(i-1, j) + f(i, j-1)
    需要注意的是，如果 i=0，那么 f(i-1,j) 并不是一个满足要求的状态，我们需要忽略这一项；同理，如果 j=0，那么 f(i,j-1)
    并不是一个满足要求的状态，我们需要忽略这一项。
    初始条件为 f(0,0)=1，即从左上角走到左上角有一种方法。
    最终的答案即为 f(m-1,n-1)f(m−1,n−1)。
    """
    dp = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]


def uniquePaths2(m, n):
    """
    官方解法2：组合数学
    从左上角到右下角的过程中，我们需要移动 m+n-2 次，其中有 m-1 次向下移动，n-1 次向右移动。因此路径的总数，
    就等于从 m+n-2 次移动中选择 m-1 次向下移动的方案数，即组合数：

    """
    pass


def main():
    m = 3
    n = 7
    m = 3
    n = 2
    # m = 7
    # n = 3
    # m = 3
    # n = 3
    # m = 1
    # n = 1
    res = uniquePaths2(m, n)
    print(res)


if __name__ == '__main__':
    main()
