"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

回溯法：一种通过探索所有可能的候选解来找出所有的解的算法。如果候选解被确认不是一个解（或者至少不是最后一个解），
回溯算法会通过在上一步进行一些变化抛弃该解，即回溯并且再次尝试。

链接：https://leetcode-cn.com/problems/permutations/solution/quan-pai-lie-by-leetcode-solution-2/
"""


def permute(nums):
    """
    官方解法
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(first=0):
        # 所有数都填完了
        if first == n:
            res.append(nums[:])
        for i in range(first, n):
            # 动态维护数组
            nums[first], nums[i] = nums[i], nums[first]
            # 继续递归填下一个数
            backtrack(first + 1)
            # 撤销操作
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    res = []
    backtrack()
    return res


def main():
    nums = [1, 2, 3]
    res = permute(nums)
    print(res)


if __name__ == '__main__':
    main()
