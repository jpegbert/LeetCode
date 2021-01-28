"""
最接近的三数之和

题目描述：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与target最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

思路：
先排序，确定第一个元素a。然后在剩下的元素中找b和c。b从a之后的第一个元素向后找，c从最终一个元素向前找，当sum(a + b + c) > target时，
c指针向左移，否则b指针向后移
链接：https://leetcode-cn.com/problems/3sum-closest

"""


def threeSumClosest(nums, target):
    """
    官方解法，已AC
    """
    nums = sorted(nums)
    res = 0
    diff = float("inf")
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: # 两个数字相等
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return s
            tmp_diff = abs(s - target)
            if diff > tmp_diff:
                diff = tmp_diff
                res = s
            if s > target:
                k0 = k - 1
                while j < k0 and nums[k0] == nums[k]:
                    k0 -= 1
                k = k0
            else:
                j0 = j + 1
                while j0 < k and nums[j] == nums[j0]:
                    j0 += 1
                j = j0
    return res


def main():
    # nums = [-1, 2, 1, -4]
    # target = 1 # 2
    # nums = [1, 1, -1, -1, 3]
    # target = -1 # -1
    # nums = [1, 1, 1, 0]
    # target = 100 # 3
    nums = [0, 1, 2]
    target = 3 # 3
    res = threeSumClosest(nums, target)
    print(res)


if __name__ == '__main__':
    main()
