"""
题目描述：
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字0之外，这两个数都不会以0开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

思路：
数字是存储在逆序排序的链表中，所以直接从头到尾遍历链表，并相加，即可得到最终结果的逆序结果
注意：进位值需要最后再判断一次
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def add(l1, l2):
    """
    一般方法
    :param l1:
    :param l2:
    :return:
    """
    jinwei = 0
    result = ListNode(-1)
    tmp_node = result
    while l1 and l2:
        tmp = l1.val + l2.val + jinwei
        if tmp >= 10:
            jinwei = int(tmp / 10)
            tmp = int(tmp % 10)
        else:
            jinwei = 0
        node = ListNode(tmp)
        tmp_node.next = node
        tmp_node = node
        l1 = l1.next
        l2 = l2.next
    while l1 is not None:
        tmp = l1.val + jinwei
        if tmp >= 10:
            jinwei = int(tmp / 10)
            tmp = int(tmp % 10)
        else:
            jinwei = 0
        node = ListNode(tmp)
        tmp_node.next = node
        tmp_node = node
        l1 = l1.next
    while l2 is not None:
        tmp = l2.val + jinwei
        if tmp >= 10:
            jinwei = int(tmp / 10)
            tmp = int(tmp % 10)
        else:
            jinwei = 0
        node = ListNode(tmp)
        tmp_node.next = node
        tmp_node = node
        l2 = l2.next
    if jinwei > 0:
        node = ListNode(jinwei)
        tmp_node.next = node
        tmp_node = node
    return result.next


def add1(l1, l2):
    """
    优化后的方法
    :param l1:
    :param l2:
    :return:
    """
    jinwei = 0
    result = ListNode(-1)
    tmp_node = result
    while l1 or l2:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        tmp = a + b + jinwei
        if tmp >= 10:
            jinwei = int(tmp / 10)
            tmp = int(tmp % 10)
        else:
            jinwei = 0
        node = ListNode(tmp)
        tmp_node.next = node
        tmp_node = node
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if jinwei > 0:
        node = ListNode(jinwei)
        tmp_node.next = node
        tmp_node = node
    return result.next


def main():
    head1 = ListNode(1)
    tmp = head1
    for i in range(3): # 1012 2101
        node = ListNode(i)
        tmp.next = node
        tmp = node
    head2 = ListNode(5)
    tmp = head2
    for i in range(6, 8): # 567 765
        node = ListNode(i)
        tmp.next = node
        tmp = node
    # while head2 is not None:
    #     print(head2.val)
    #     head2 = head2.next
    res = add(head1, head2)
    print(res)




if __name__ == '__main__':
    main()
