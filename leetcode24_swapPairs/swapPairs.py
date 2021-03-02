"""
两两交换链表中的节点

题目描述：
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]
 
提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    """
    方法1：交换节点的值
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    dummyNode = ListNode(-1, None)
    dummyNode.next = head
    currNode = head
    while currNode is not None and currNode.next:
        t = currNode.val
        currNode.val = currNode.next.val
        currNode.next.val = t
        currNode = currNode.next.next
    return dummyNode.next


def swapPairs1(head):
    """
    方法2：递归
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    next = head.next
    head.next = swapPairs1(next.next)
    next.next = head
    return next


def swapPairs2(head):
    """
    方法3：不修改节点的值（这是除了递归方法之外最佳的解法）
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head
    dummyHead = ListNode(-1, None)
    dummyHead.next = head
    temp = dummyHead
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return dummyHead.next


def create_list(data):
    if data is None or len(data) <= 0:
        return None
    head = ListNode(data[0], None)
    tmp_node = head
    for i in range(1, len(data)):
        curr_node = ListNode(data[i], None)
        tmp_node.next = curr_node
        tmp_node = curr_node
    return head


def print_list(head):
    if head is None:
        return
    tmp_node = head
    while tmp_node:
        print(tmp_node.val)
        tmp_node = tmp_node.next


def main():
    head = [1, 2, 3, 4]
    # head = []
    # head = [1]
    # head = [1, 2, 3]
    head = create_list(head)
    print_list(head)
    res = swapPairs2(head)
    print("------")
    print_list(res)


if __name__ == '__main__':
    main()
