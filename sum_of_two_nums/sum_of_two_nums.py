"""
题目描述：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


def two_sum(nums, target):
    """
    这种适用于数组是有序的
    :param nums:
    :param target:
    :return:
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return [i, j]
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return []


def two_sum1(nums, target):
    """
    解法1：暴力法
    :param nums:
    :param target:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return []


def two_sum2(nums, target):
    """
    哈希法：第一次把数组的元素和索引存储在哈希表中，第二次遍历数组查询哈希表中是否存在对应key的元素
    :param nums:
    :param target:
    :return:
    """
    my_dict = {}
    for i in range(len(nums)):
        my_dict[nums[i]] = i
    for i in range(len(nums)):
        tmp = target - nums[i]
        # 同一个元素不能使用两遍,所以对比的是下标
        if my_dict.get(tmp) is not None and i != my_dict.get(tmp):
            return [i, my_dict.get(tmp)]
    return []


def two_sum3(nums, target):
    """
    暴力法的优化解法：遍历到一个数字后，不用再循环一次数组，在python中可以直接判断 (目标值 - 当前位置元素) 是否在数组中，丙求出位置
    :param nums:
    :param target:
    :return:
    """
    j = -1
    for i in range(len(nums)):
        if (target - nums[i]) in nums:
            j = nums.index(target - nums[i])
            if i != j:
                break
    if j >= 0:
        return [i, j]
    else:
        return []


def main():
    arr = [22, 19, 7, 11, 15]
    result = two_sum3(arr, 41)
    print(result)


if __name__ == '__main__':
    main()
