"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。


示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""



def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def backtrack(nums, used, cur, n):
        if cur == n:
            res.append(tmp)
            return
        for i in range(n):
            print(i)
            # 判重
            if used[i]:
                continue
            # // 剪枝, i>0 是为了让 nums[i-1] 不越界
            # 正常不剪枝的回溯: 对于每一层回溯搜索, 会判断其它未被使用的所有元素(会有重复的元素), 都被填充到该位置一次;
            # 剪枝的意思是: 保证相邻的重复元素在每一层的回溯搜索中, 只被回溯搜索填充一个, 其余的不再会填充, 且遵循靠左的第一个未被填充的元素被填充,
            # 若没有这个剪枝的过程, 那么这些重复的相邻元素, 会被回溯搜索填充cnt(相邻重复元素)次;
            # eg: 对于重复的四个元素 [0, 0, 0, 0], (0 表示未填充) 第一层回溯填充第一个0, 第二层回溯第一个0因已被used, 即continue, 第二个0不会被continue, 执行回溯
            # [0, 0, 0, 0] -> [1, 0, 0, 0] -> [1, 1, 0, 0] -> [1, 1, 1, 0] -> [1, 1, 1, 1] (1 表示填充)
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            tmp.append(nums[i])
            used[i] = True
            # 进入下一层
            backtrack(nums, used, cur + 1, n)
            used[i] = False
            # 恢复原来的状态
            tmp.remove(tmp[-1])

    res = []
    tmp = []
    n = len(nums)
    used = [False for i in range(len(nums))]
    nums = sorted(nums)
    print("nums: ", nums)
    backtrack(nums, used, 0, n)
    return res


def main():
    nums = [1, 1, 2]
    res = permuteUnique(nums)
    print(res)


if __name__ == '__main__':
    main()
