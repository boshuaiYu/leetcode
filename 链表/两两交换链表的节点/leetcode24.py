"""
    给定一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        pre = dummy_head
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next
            cur.next = post.next
            post.next = cur
            pre.next = post
            pre = pre.next.next

        return dummy_head.next