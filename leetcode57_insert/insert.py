"""
57. 插入区间
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

示例 2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

示例 3：
输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

示例 4：
输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

示例 5：
输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]

提示：
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
"""


def insert(intervals, newInterval):
    """
    官方解法：已AC
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    left, right = newInterval
    placed = False
    ans = list()
    for li, ri in intervals:
        if li > right:
            # 在插入区间的右侧且无交集
            if not placed:
                ans.append([left, right])
                placed = True
            ans.append([li, ri])
        elif ri < left:
            # 在插入区间的左侧且无交集
            ans.append([li, ri])
        else:
            # 与插入区间有交集，计算它们的并集
            left = min(left, li)
            right = max(right, ri)

    if not placed:
        ans.append([left, right])
    return ans


def insert1(intervals, newInterval):
    """
    在官方解法的基础上：调换if else的顺序，还是可以的，已经AC
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    left, right = newInterval
    placed = False
    ans = list()
    for li, ri in intervals:
        if ri < left:# 在插入区间的左侧且无交集
            ans.append([li, ri])
        elif li > right:
            # 在插入区间的右侧且无交集
            if not placed:
                ans.append([left, right])
                placed = True
            ans.append([li, ri])
        else:
            # 与插入区间有交集，计算它们的并集
            left = min(left, li)
            right = max(right, ri)

    if not placed:
        ans.append([left, right])
    return ans


def main():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5] # [[1, 5], [6, 9]]
    # intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    # newInterval = [4, 8]
    res = insert(intervals, newInterval)
    print(res)


if __name__ == '__main__':
    main()
