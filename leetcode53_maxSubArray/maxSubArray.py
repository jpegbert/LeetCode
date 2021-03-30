"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

示例 2：
输入：nums = [1]
输出：1

示例 3：
输入：nums = [0]
输出：0

示例 4：
输入：nums = [-1]
输出：-1

示例 5：
输入：nums = [-100000]
输出：-100000

提示：
1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
"""


def maxSubArray(nums):
    """
    官方解法1：动态规划
    用 f(i) 代表以第 i 个数结尾的「连续子数组的最大和」
    """
    last = 0
    max_sum = float('-inf')
    for num in nums:
        last = max(last + num, num)
        max_sum = max(last, max_sum)
    return max_sum


# 更容易理解的解法
def maxSubArray1(nums):
    """
    已AC
    :param nums:
    :return:
    """
    max_sum = nums[0]
    last = nums[0]
    for i in range(1, len(nums)):
        if last < 0:
            last = nums[i]
        else:
            last = last + nums[i]
        max_sum = max(max_sum, last)
    return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray1(nums)
    print(res)


if __name__ == '__main__':
    main()
