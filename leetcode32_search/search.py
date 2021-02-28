"""
33. 搜索旋转排序数组

题目描述：
整数数组 nums 按升序排列，数组中的值 互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。


示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4

进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
"""


def search(nums, target):
    """
    自己的解法，已经AC
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target >= nums[0]:
        i = 0
        while i < len(nums) and target >= nums[i]:
            if i > 0 and nums[i] < nums[i - 1]:
                break
            if nums[i] == target:
                return i
            i += 1
    elif target <= nums[-1]:
        i = len(nums) - 1
        while i >= 0 and target <= nums[i]:
            if i < len(nums) - 1 and nums[i] > nums[i + 1]:
                break
            if nums[i] == target:
                return i
            i -= 1
    return -1


def search1(nums, target):
    """
    官方解法，二分法
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[0] <= nums[mid]: # 说明在[0,mid]是严格升序，也就是在旋转后数组的前半边
            if nums[0] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else: # 说明在[mid,len(nums)]是严格升序，也就是在旋转后数组的后半边
            if nums[mid] < target <= nums[len(nums) - 1]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0 # 4
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3 # -1
    nums = [1]
    target = 0 # -1
    res = search1(nums, target)
    print(res)


if __name__ == '__main__':
    main()
