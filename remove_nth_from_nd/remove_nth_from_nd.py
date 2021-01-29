"""

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
 
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """
    官方解法 已AC
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head is None or n <= 0:
        return None
    # 虚拟头结点
    dummy_head = ListNode(0, head)
    fast = head
    slow = dummy_head
    for i in range(n):
        if fast:
            fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy_head.next


def create_list(data):
    if len(data) == 0:
        return None
    head = ListNode(data[0], None)
    node = head
    for i in range(1, len(data)):
        curr_node = ListNode(data[i], None)
        node.next = curr_node
        node = curr_node
    return head


def main():
    head = [1, 2, 3, 4, 5]
    n = 2
    head = create_list(head)
    res = removeNthFromEnd(head, n)
    t = res
    while t:
        print(t.val, end=" ")
        t = t.next


if __name__ == '__main__':
    main()
