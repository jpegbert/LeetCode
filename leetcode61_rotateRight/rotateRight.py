"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]

提示：
链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    """
    官方解法：闭合为环，已AC

    :type head: ListNode
    :type k: int
    :rtype: ListNode

    记给定链表的长度为 n，注意到当向右移动的次数 k≥n 时，我们仅需要向右移动 k % n 次即可。因为每 n 次移动都会让链表变为原状。
    这样我们可以知道，新链表的最后一个节点为原链表的第 (n - 1) - (k % n) 个节点（从 0 开始计数）。
    这样，我们可以先将给定的链表连接成环，然后将指定位置断开。
    具体代码中，我们首先计算出链表的长度 n，并找到该链表的末尾节点，将其与头节点相连。这样就得到了闭合为环的链表。
    然后我们找到新链表的最后一个节点（即原链表的第 (n - 1) - (k % n) 个节点），将当前闭合为环的链表断开，即可得到我们所需要的结果。
    特别地，当链表长度不大于 1，或者 k 为 n 的倍数时，新链表将与原链表相同，我们无需进行任何处理。
    """
    if k == 0 or not head or not head.next:
        return head

    n = 1
    cur = head
    while cur.next:
        cur = cur.next
        n += 1 # n是末尾节点

    # 找到移动k位后新链表的最后一个节点
    add = n - k % n # add记录的是新链表的最后一个节点
    if add == n: # 如果k正好是n的整数倍数，新链表将于原链表返回
        return head

    cur.next = head # 将原链表闭合成环
    while add: # 把指针指向新链表最后一个节点的位置
        cur = cur.next
        add -= 1

    ret = cur.next # 此时ret是移动k位后新链表的头
    cur.next = None # 将环断开
    return ret


def create_list(head):
    if head is None or len(head) == 0:
        return None
    new_head = ListNode(head[0])
    tmp_node = new_head
    for i in range(1, len(head)):
        curr_node = ListNode(head[i])
        tmp_node.next = curr_node
        tmp_node = curr_node
    tmp_node.next = None
    return new_head


def print_list(head):
    while head is not None:
        print(head.val)
        head = head.next


def main():
    head = [1, 2, 3, 4, 5]
    k = 6
    # head = [0, 1, 2]
    # k = 4
    # head = []
    # k = 0
    # head = [1, 2]
    # k = 0
    head = create_list(head)
    # print_list(head)
    head = rotateRight(head, k)
    print_list(head)


if __name__ == '__main__':
    main()
