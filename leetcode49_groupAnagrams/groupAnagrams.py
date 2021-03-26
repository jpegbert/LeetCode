"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
所有输入均为小写字母。
不考虑答案输出的顺序。
"""


def groupAnagrams(strs):
    """
    方法1：排序
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res_dcit = {}
    for item in strs:
        sorted_item = "".join(sorted(item))
        if sorted_item not in res_dcit.keys():
            curr_list = []
        else:
            curr_list = res_dcit[sorted_item]
        curr_list.append(item)
        res_dcit[sorted_item] = curr_list
    res_list = []
    for key, word_list in res_dcit.items():
        res_list.append(word_list)
    return res_list


def groupAnagrams1(strs):
    """
    方法2：计数
    字母一共就26个，字母异位词只是字母的位置不一样，字母完全一样，所以可以统计字符串中出现字母次数一样，就表示是同一组
    """
    import collections
    mp = collections.defaultdict(list)

    for st in strs:
        counts = [0] * 26
        for ch in st:
            counts[ord(ch) - ord("a")] += 1
        # 需要将 list 转换成 tuple 才能进行哈希
        mp[tuple(counts)].append(st)
    return list(mp.values())


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = groupAnagrams1(strs)
    print(res)


if __name__ == '__main__':
    main()
