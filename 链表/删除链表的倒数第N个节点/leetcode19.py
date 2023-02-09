"""
    给定一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        fast, slow = dummy_head, dummy_head
        while n > 0 and fast:
            fast = fast.next
            n -= 1

        fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy_head.next
