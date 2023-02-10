# 数组
##  基础内容
注意点：数组下标都是从0开始的；数组内存空间的地址是连续的。

因为数组的在内存空间的地址是连续的，所以我们在删除或者增添元素的时候，就难免要移动其他元素的地址，因此数组的元素是不能删的，只能覆盖

---
## Day1
 * [leetcode704](https://leetcode.cn/problems/binary-search/)二分法：给定一个<font color ="orange">有序数组</font>,同时一般数组无重复元素，一旦出现重复数组，可能返回的下标并不唯一可参考[leetcode34](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)

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


 * [leetcode27](https://leetcode.cn/problems/remove-element/)双指针法：通过一个快指针和慢指针在一个for循环下完成两个for循环的工作，双指针法也可分为快慢指针和左右指针

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
* [leetcode977](https://leetcode.cn/problems/squares-of-a-sorted-array/)有序数组的平方：给定一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
了解题目中可以直到有序数组平方的最大值一定分布在左右(类似于二次函数)。因为数组是有序的，只不过负数平方之后可能成为最大数了。那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。

   参考动画过程：https://code-thinking.cdn.bcebos.com/gifs/977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.gif
   ```
   class Solution:
       def sortedSquares(self, nums: List[int]) -> List[int]:
         result = [-1] * len(nums)  # 新创建一个与原列表长度相同的新列表
         left, right, k = 0, len(nums) - 1, len(nums) - 1   # 分别定义左右指针位置及新数组中最大值的索引
         while left <= right:
            if nums[left] ** 2 >= nums[right} ** 2:  # 说明更大值在左边
               result[k] = nums[left] ** 2
               left += 1  # 将左指针向右移动一位
            else:
               result[k] = nums[right] ** 2
               right -= 1  # 将右指针向右移动一位
            k -= 1
         
         return result
   ```
   参考文档资料：https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html
   
   参考视频：https://www.bilibili.com/video/BV1QB4y1D7ep
* [leetcode209](https://leetcode.cn/problems/minimum-size-subarray-sum/)长度最小的连续子数组：滑动窗口法。所谓滑动窗口，就是不断的调节子序列的起始位置和终止位置，从而得出要想的结果
   
   参考动画过程：https://code-thinking.cdn.bcebos.com/gifs/209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.gif
   
   滑动窗口的关键点是<font color ="LightPink">起始点与终点的定位</font>。先固定起始点不动，找到符合条件的最大长度；后保持终点不动，连续移动起始点直至找到最小长度
   ```
  class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      length = 1e5 + 1  # length题目中最大1e5 等同于float("inf")  定义一个无限大的数
      result = 0  
      left = 0  # 定义起始指针位置
      for right in range(len(nums))：
        result += nums[right]
        while result >= target:
            length = min(length, j-i+1)  # 找到最小长度
            sum -= nums[left]
            left += 1
      return 0 if length > 1e5 + 1 else length  # 如果没找到返回0，反之返回最小长度
  ```
    参考文档资料：https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html
  
    参考视频：https://www.bilibili.com/video/BV1tZ4y1q7XE

    <font color ="LightBlue">解法2(前缀和+二分查找)二刷时再学习！！！</font>

* [leetcode59](https://leetcode.cn/problems/spiral-matrix-ii/)螺旋矩阵关键点：<font color ="LightPink">循环次数；循环不变量</font>循环遵循左闭右开的思路，保证循环的完整性
    ```
  class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[-1] * n for _ in range(n)]
        start_x, start_y, count  = 0, 0, 1 # 定义循环起始点及计数起点
        loop, mid = n // 2, n // 2  # 迭代次数与n有关，而奇数偶数区别在于中心的值
        for offset in range(1, loop+1):  # 每循环一圈offset要加1
            for i in range(start_x, n-offset):  # 从左到右, 保证第一个维度保持不变，即start_x
                nums[start_x][i] = count
                count += 1
            for i in range(start_y, n_offset):  # 从上到下, 保持第二个维度不变，即n-offset
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset, start_y, -1):  # 从右到左，保持第一个维度不变，由于在最下面，即n-offset
                nums[n-offset][i] = count
                count += 1
            for i in range(n-offset, start_x, -1):  # 从下到上，保持第二个维度不变，由于在最左边，即start_y
                nums[i][start_y] = count
                count += 1
            start_x += 1
            start_y += 1
        
        if n % 2 != 0:
            nums[mid][mid] = count
  
        return nums 
  ```
    参考文档资料：https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html

    参考视频资料：https://www.bilibili.com/video/BV1SL4y1N7mV/
---
# 数组总结
1. 数组是存放在连续内存空间上的相同类型数据的集合(与后面的链表不同)
2. 因为数组的在内存空间的地址是连续的，所以我们在删除或者增添元素的时候，就难免要移动其他元素的地址，而且数组的元素是不能删的，只能覆盖