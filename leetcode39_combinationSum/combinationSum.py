"""
39. 组合总和

题目描述
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    res = []
    helper(0, 0, [], candidates, target, res)
    return res


def helper(index, cur_sum, cur_list, candidates, target, res):
    """
    :param i: 当前考察的元素
    :param cur_sum: 当前和
    :param cur_list: 获得cur_sum所用的元素
    :return:
    """
    # 跳出循环的条件
    if cur_sum > target or index == len(candidates):
        return

    # 如果找到符合条件的子数组，则添加到结果中
    if cur_sum == target:
        res.append(cur_list)
        return

    # 考虑当前元素candidates[i]
    helper(index, cur_sum + candidates[index], cur_list + [candidates[index]], candidates, target, res)

    # 不考虑当前元素
    helper(index + 1, cur_sum, cur_list, candidates, target, res)


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    res = combinationSum(candidates, target)
    print(res)


if __name__ == '__main__':
    main()
