"""
寻找两个正序数组的中位数

题目描述：
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0
示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def findMedianSortedArrays(nums1, nums2):
    all_ = nums1 + nums2
    m = len(nums1)
    n = len(nums2)
    all_.sort()
    if (m + n) % 2 == 0:
        print(all_[int((m + n) / 2) - 1], all_[int((m + n) / 2)])
        return (all_[int((m + n) / 2) - 1] + all_[int((m + n) / 2)]) / 2.0
    else:
        return all_[int((m + n) / 2)]


def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    res = findMedianSortedArrays(nums1, nums2)
    print(res)


if __name__ == '__main__':
    main()
