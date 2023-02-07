# 链表
## 基础知识
链表是一种通过指针串联在一起的线性结构，每一个节点由两部分组成，一个是数据域一个是指针域（存放指向下一个节点的指针），最后一个节点的指针域指向null（空指针的意思）

链表的入口节点称为链表的头结点也就是head

与数组不同，数组是在内存中是连续分布的，但是链表在内存中可不是连续分布的。而链表是通过指针域的指针链接在内存中各个节点。所以链表中的节点在内存中不是连续分布的 ，而是散乱分布在内存中的某地址上，分配机制取决于操作系统的内存管理
![img.png](img.png)
节点（ node）是构建链表的基本数据结构。每一个节点对象都必须持有至少两份信息。节点必须包含列表元素，我们称之为节点的数据变量。同时节点必须保存指向下一个节点的引用。
以下定义ListNode：
```
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
```
## Day 3
* [leetcode707](https://leetcode.cn/problems/design-linked-list/)设计链表：包含了链表的5个操作

    * get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    * addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    * addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    * addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    * deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
    
   以下以单链表的设计为例：(双链表设计参考"./leetcode707.py")
   ```
   class Node(object):  # 定义Node数据结构，其中包含两个属性：当前值(val); 下一个Node的指针(next)
       def __init__(self, val):
           self.val = val
           self.next = None
            
   class MyLinkedList:
    
       def __init__(self):  # 初始定义链表属性：虚拟头节点(head)及链表长度(size)
           self.head = Node(0)  # 定义头节点的值为0
           self.size = 0
    
       def get(self, index: int) -> int:
           if index < 0 or index >= self.size:
               return -1
           else:
               cur = self.head.next  # 指针指向head后的Node, 也是链表的第一个元素
           while index:
               cur = cur.next  # 通过指针移动找到对应index的Node(技巧：若要找对应索引的Node,循环起始从第一个Node开始；找到前一个，循环起始从head开始)
               index -= 1
           return cur.val
    
       def addAtHead(self, val: int) -> None:
           new_node = Node(val)  # 添加值为val的新Node
           new_node.next = self.head.next  # 新增加的Node先连接, 先保证链表完整
           self.head.next = new_node   # 改变head连接
           self.size += 1  # 链表长度+1
    
       def addAtTail(self, val: int) -> None:
           cur = self.head
           new_node = Node(val)
           while cur.next:  # 当cur的next不为None就一直循环，直到cur指向链表最后一个Node
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
           while index:  # 同get方法，找到对应index前一个Node(循环起始从head开始)
               cur = cur.next
               index -= 1
           new_node.next = cur.next
           cur.next = new_node
           self.size += 1
    
       def deleteAtIndex(self, index: int) -> None:
           if index < 0 or index >= self.size:
               return
           cur = self.head
           while index:  # 找到index前一个Node
               cur = cur.next
               index -= 1
           cur.next = cur.next.next
           self.size -= 1
   ```
  参考文档资料：https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html

  参考视频：https://www.bilibili.com/video/BV1FU4y1X7WD/
* [leetcode203](https://leetcode.cn/problems/remove-linked-list-elements/)移除链表元素: