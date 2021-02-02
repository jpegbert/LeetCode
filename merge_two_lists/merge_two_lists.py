"""
合并两个有序链表

题目描述：
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
 
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列


链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    """
    自己的解法，已AC
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None and l2 is None:
        return None
    elif l1 is not None and l2 is None:
        return l1
    elif l1 is None and l2 is not None:
        return l2
    else:
        prehead = ListNode(-1, None)
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next = l2

    return prehead.next


def mergeTwoLists(l1, l2):
    """
    官方解法：递归
    :param l1:
    :param l2:
    :return:
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


def mergeTwoLists(l1, l2):
    """
    官方解法
    :param l1:
    :param l2:
    :return:
    """
    prehead = ListNode(-1)
    prev = prehead
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 if l1 is not None else l2

    return prehead.next


def createList(data):
    if len(data) == 0:
        return None
    head = ListNode(data[0], None)
    dummyNode = head
    for i in range(1, len(data)):
        currNode = ListNode(data[i], None)
        dummyNode.next = currNode
        dummyNode = currNode
    return head


def printList(head):
    while head:
        print(head.val)
        head = head.next


def main():
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    # l1 = []
    # l2 = []
    # l1 = []
    # l2 = [0]
    l1 = createList(l1)
    l2 = createList(l2)
    # printList(l1)
    # print("==")
    # printList(l2)
    res = mergeTwoLists(l1, l2)
    printList(res)


if __name__ == '__main__':
    main()
