# 数组
##  基础内容
注意点：数组下标都是从0开始的；数组内存空间的地址是连续的。

因为数组的在内存空间的地址是连续的，所以我们在删除或者增添元素的时候，就难免要移动其他元素的地址，因此数组的元素是不能删的，只能覆盖
## Day1
 * (leetcode704)二分法：给定一个<font color ="orange">有序数组</font>,同时一般数组无重复元素，一旦出现重复数组，可能返回的下标并不唯一(可参考leetcode34)

    二分法的重点是：<font color ="orange">边界条件的界定</font>

    比如：
        1. 循环判断中是 left < right 还是 left <= right
        2. 分区间更新的时候是 right = middle 还是 right = middle -1
    
    关键就是循环不变量原则：<font color = "orange">要在二分查找的过程中，保持不变量，就是在while寻找中每一次边界的处理都要坚持根据区间的定义来操作</font>
    
    解法：以下仅展示左闭右闭写法，其他详见"./leetcode704.py"文件中
    ```
   # 左闭右闭
    class Solutions(object):
      def binarySearch(self,nums:List[int], target:int): --> int
            left, right = 0, len(nums) - 1  # 此时right表示的是数组最后一个元素的下标，定义区间为[left, right]
            while left <= right:   # 当left == right时是符合该区间定义的，即符合循环不变量原则
                middle = left + (right - left) // 2  # 防止因right过大而造成溢出 等同于int((right + left) / 2)
                if nums[middle] < target:   # target在右区间，而此时明确nums[middle] != target
                    left = middle + 1 # 区间更新为[middle + 1, right]
                elif nums[middle] > target:  # target在左区间同理
                    right = middle - 1  
                else:
                    return middle
            return -1  # 未找到目标值返回-1
    ```
    参考文档资料：https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
    
    参考视频资料：https://www.bilibili.com/video/BV1fA4y1o715


 * (leetcode27)双指针法：通过一个快指针和慢指针在一个for循环下完成两个for循环的工作，双指针法也可分为快慢指针和左右指针

   定义快慢指针：
    * 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
    * 慢指针：指向更新 新数组下标的位置
   
    <font color = "orange">双指针法（快慢指针法）在数组和链表的操作中是非常常见的，很多考察数组、链表、字符串等操作的面试题，都使用双指针法。</font>
    
    以快慢指针为例，以下代码：
    ```
   class Solutions(object):
      def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast = 0, 0  # 先定义一个快指针和慢指针
        while fast < len(nums):  # 用快指针遍历数组中的所有元素
            if nums[fast] != val:  # 遇到非移除值时给慢指针所在位置赋值
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow  # 慢指针此时指向的最终数组的末尾，也就是新数组的有效长度
    ```
   快慢双指针的过程是数组值的覆盖，而不是交换！

   参考文档资料：https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html

   参考视频资料：https://www.bilibili.com/video/BV12A4y1Z7LP

   <font color ="LightPink">算法题中(尤其是python)，如果调库函数是算法实现过程的一小部分，可以直接调用库函数，但要清楚库函数的时间与空间复杂度；但为实现某库函数的性质，
   不要使用库函数实现</font>
---
## Day 2