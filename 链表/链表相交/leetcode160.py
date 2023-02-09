"""
    给定两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null
"""


# 解法1.创建两个指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1, cur2 = headA, headB
        lenA, lenB = 0, 0
        while cur1:
            cur1 = cur1.next
            lenA += 1
        while cur2:
            cur2 = cur2.next
            lenB += 1

        if lenB >= lenA:
            sub = lenB - lenA
            cur1, cur2 = headA, headB
            while sub > 0:
                cur2 = cur2.next
                sub -= 1
        else:
            sub = lenA - lenB
            cur1, cur2 = headA, headB
            while sub > 0:
                cur1 = cur1.next
                sub -= 1

        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            else:
                cur1 = cur1.next
                cur2 = cur2.next

        return None


# 解法2：一个指针
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:  # 求链表A的长度
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:  # 求链表B的长度
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:  # 让curB为最长链表的头，lenB为其长度
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):  # 让curA和curB在同一起点上（末尾位置对齐）
            curB = curB.next
        while curA:  # 遍历curA 和 curB，遇到相同则直接返回
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
