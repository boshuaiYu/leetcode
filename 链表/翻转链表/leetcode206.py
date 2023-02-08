"""
    给定单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""


# 解法1.双指针法

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        return pre


# 解法2：递归法

# Definition for singly-linked list.
class ListNode1:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, pre):  # 定义交换函数
            if cur is None:  # 定义递归出口，当cur指向None时退出，与双指针的循环结束一样
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(temp, cur)  # pre与cur的位置更新，新的cur移动到temp位置，而pre移动到原来cur位置

        return reverse(head, None)  # cur起始值，pre起始值为head和None
