"""
34. 在排序数组中查找元素的第一个和最后一个位置

题目描述：
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9
"""


def searchRange(nums, target):
    """
    自己的解法，已AC
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0:
        return [-1, -1]
    l, r = 0, len(nums)
    while l >= 0 and l < len(nums) and l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            i = mid - 1
            while i >= 0 and nums[i] == target:
                i -= 1
            i += 1
            j = mid + 1
            while j < len(nums) and nums[j] == target:
                j += 1
            j -= 1
            return [i, j]
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return [-1, -1]


def searchRange1(nums, target):
    leftIdx = binarySearch(nums, target, True)
    rightIdx = binarySearch(nums, target, False) - 1
    if leftIdx <= rightIdx and rightIdx < len(nums) and nums[leftIdx] == target and nums[rightIdx] == target:
        return [leftIdx, rightIdx]
    return [-1, -1]


def binarySearch(nums, target, lower):
    left = 0
    right = len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target or (lower and nums[mid] >= target):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return ans




def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8 # [3, 4]
    nums = [5, 7, 7, 8, 8, 10]
    target = 6  # [-1, -1]
    nums = []
    target = 0 # [-1, -1]
    nums = [2, 2]
    target = 3  # [-1, -1
    res = searchRange1(nums, target)
    print(res)


if __name__ == '__main__':
    main()
