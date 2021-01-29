

def fourSum(nums, target):
    """
    官方解法 已AC
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums) == 0:
        return list()
    nums = sorted(nums)
    res = []
    length = len(nums)
    for i in range(length - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]) > target:
            break
        if (nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1]) < target:
            continue
        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2]) > target:
                break
            if (nums[i] + nums[j] + nums[length - 2] + nums[length - 1]) < target:
                continue
            left, right = j + 1, length - 1
            while left < right:
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                if sum == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

    return res


def main():
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    res = fourSum(nums, target)
    print(res)


if __name__ == '__main__':
    main()
