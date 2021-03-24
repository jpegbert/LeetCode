"""
45. 跳跃游戏 II

给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

说明:
假设你总是可以到达数组的最后一个位置。

https://leetcode-cn.com/problems/jump-game-ii/
"""


def jump(nums):
    """
    官方解法1：反向查找出发位置
    :type nums: List[int]
    :rtype: int
    """
    position = len(nums) - 1
    steps = 0
    while position > 0:
        for i in range(position):
            if i + nums[i] >= position:
                position = i
                steps += 1
                break
    return steps


def jump1(nums):
    """
    官方解法2：正向查找可到达的最大位置
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    maxPos, end, step = 0, 0, 0
    for i in range(n - 1):
        if maxPos >= i:
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
    return step


def jump2(nums):
    """
    官方解法2的另一种写法
    :param nums:
    :return:
    """
    n = len(nums) - 1
    max_pos = 0
    step = now = end = 0
    while end < n:
        max_pos = max(max_pos, nums[now] + now)
        if now == end:
            step += 1
            end = max_pos
        now += 1
    return step


def main():
    nums = [2, 3, 1, 1, 4]
    res = jump2(nums)
    print(res)


if __name__ == '__main__':
    main()
