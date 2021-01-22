"""
题目描述：
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 
(i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

链接：https://leetcode-cn.com/problems/container-with-most-water

思路：
双指针法。两个指针分别指向数据的第一个和最后一个，此时围成的面积是 两个指针指向的高度的较小的一个 * 两个指针指向位置的横坐标的距离。
然后，移动两个指针的一个，要移动哪个取决于 当前两个指针指向的位置哪个元素的高度小，因为高度大的盛水多
"""


def max_area(height):
    if len(height) <= 0:
        return 0
    left = 0
    right = len(height) - 1
    res = -1
    tmp = -1
    while left < right:
        tmp = min(height[left], height[right]) * (right - left)
        if tmp > res:
            res = tmp
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = max_area(height)
    print(res)


if __name__ == '__main__':
    main()
