"""
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，
并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。


示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

提示：
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""


def merge(intervals):
    """
    自己的解法，已AC
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals = sorted(intervals, key=lambda x: x[0], reverse=False)
    i = 1
    res = [intervals[0]]
    while i < len(intervals):
        last = res[-1]
        curr = intervals[i]
        if last[1] >= curr[0]:
            # 这里要注意这种case出现 [[1, 4], [2, 3]]，前一个的end比后一个end还小
            new_val = [last[0], max(curr[1], last[1])]
            res.remove(res[-1])
            res.append(new_val)
        else:
            res.append(curr)
        i += 1
    return res


def merge(intervals):
    """
    官方解法
    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # 如果列表为空，或者当前区间与上一区间不重合，直接添加
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 否则的话，我们就可以与上一区间进行合并
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    intervals = [[1, 4], [2, 3]]
    res = merge(intervals)
    print(res)


if __name__ == '__main__':
    main()
