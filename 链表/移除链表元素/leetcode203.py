"""
    给定一个链表的头节点 head 和一个整数 val，请你删除链表中所有满足 Node.val == val的节点，并返回新的头节点 。
"""


# 解法1：使用原来的链表进行删除
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:  # 先判断头节点情况，头节点移除将头节点指针往后移一位
            head = head.next

        cur = head  # 不是头节点与设置虚拟头节点法相同
        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head  # 返回的是头节点


# 解法2：设置虚拟头节点进行删除
class ListNode1:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        cur = dummy_node
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_node.next