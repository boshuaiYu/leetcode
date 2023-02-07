"""
设计链表的实现。可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index的。
在链表类中实现这些功能：
    get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val 的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
"""


# 单链表
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head
        temp = cur.next
        cur.next = new_node
        new_node.next = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        new_node = Node(val)
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


# 双链表
class DoubleNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class MyLinkedList2:

    def __init__(self):
        self._head, self._tail = Node(0), Node(0)
        self._head.next, self._tail.pre = self._tail, self._head
        self._size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            return -1
        else:
            cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head
        temp = cur.next
        cur.next = new_node
        new_node.next = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.head
        new_node = Node(val)
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        new_node = Node(val)
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1
