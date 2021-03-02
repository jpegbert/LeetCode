"""
35. 搜索插入位置

题目描述：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。

示例 1:
输入: [1,3,5,6], 5
输出: 2

示例 2:
输入: [1,3,5,6], 2
输出: 1

示例 3:
输入: [1,3,5,6], 7
输出: 4

示例 4:
输入: [1,3,5,6], 0
输出: 0
"""



def searchInsert(nums, target):
    """
    自己的解法，已AC
    问题转化为找第一个大于等于target的位置
    由于这种解法有相等时直接返回，所以不是标准的查找第一个大于等于target的元素
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    l = 0
    r = len(nums) - 1
    t = len(nums)
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= target: # 这里不要等号也是可以的
            r = mid - 1
            t = mid
        else:
            l = mid + 1
    return t


def searchInsert1(nums, target):
    """
    官方解法
    问题转化为找第一个大于等于target的位置，这是标准的查找第一个大于等于target元素的算法
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    l = 0
    r = len(nums) - 1
    res = len(nums)
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target: # 这里不要等号也是可以的
            r = mid - 1
            res = mid
        else:
            l = mid + 1
    return res



def main():
    nums = [1, 3, 5, 7]
    target = 5 # 2
    nums = [1, 3, 5, 6]
    target = 2  # 1
    nums = [1, 3, 5, 6]
    target = 7  # 1
    res = searchInsert(nums, target)
    print(res)


if __name__ == '__main__':
    main()
