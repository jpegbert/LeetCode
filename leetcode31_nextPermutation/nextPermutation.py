"""
31. 下一个排列

题目描述：
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。


示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：
输入：nums = [1]
输出：[1]

提示：
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""


def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
        return nums
    i = len(nums) - 2
    # 从后往前找到第一个不是降序的数字位置
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0: # i >= 0 说明nums不是严格完全降序
        # 从[i + 1:len(nums)从后往前找到第一个大于nums[i]的数字位置
        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        # 两个位置的数字交换
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
    # 从1 + 1开始后面的数字是严格降序的，所以把这部分数字降序就后就是 当前排列的下一个排列
    i = i + 1
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums


def main():
    nums = [1, 2, 3]
    nums = [3, 2, 1]
    nums = [1, 3, 2]
    # nums = [1, 1, 5]
    # nums = [1]
    res = nextPermutation(nums)
    print(res)


if __name__ == '__main__':
    main()
