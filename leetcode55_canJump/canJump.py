"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。


示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

提示：
1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105
"""


def canJump(nums):
    """
    官方解法，已AC
    :param nums:
    :return:
    """
    n, rightmost = len(nums), 0
    for i in range(n):
        if i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
    return False


def canJump1(nums):
    """
    自己的解法：运行大量case是可以的，但是会超时
    """
    if len(nums) == 1:
        return True
    index_list = [0]
    while len(index_list) > 0:
        curr_idnex = index_list[0]
        index_list.remove(index_list[0])
        curr_max_step = nums[curr_idnex]
        if curr_max_step + curr_idnex >= len(nums) - 1:
            return True
        elif curr_max_step == 0 and len(index_list) == 0:
            return False
        else:
            for i in range(1, curr_max_step + 1):
                tmp_index = curr_idnex + i
                if tmp_index not in index_list:
                    index_list.append(tmp_index)

    return False


def main():
    nums = [2, 3, 1, 1, 4] # True
    nums = [3, 2, 1, 0, 4] # False
    # nums = [1, 2, 3] # True
    # nums = [1,1,2,2,0,1,1] # True
    res = canJump(nums)
    print(res)


if __name__ == '__main__':
    main()
