"""
给定一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


# 解法一：调函数法
class Solutions(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


# 时间复杂度：O(n) 空间复杂度：O(1)
# 该题其实就是要实现remove函数，该解法不推荐


# 解法2：暴力求解法
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:  # 遍历数组，每找到一个不是val的值就把count对应位置覆盖掉，同时并计数
                nums[count] = nums[i]
                count += 1

        return count


# 解法3：快慢指针法
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow

# 解法3：左右指针法(该方法可以用于交换顺序）
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            while nums[right] == val:  # 先找到右侧不是val的位置
                right -= 1
                if right < 0:
                    break
            if nums[left] == val:  # 后与left侧值为val进行互换，将val值都移到数组末尾
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    break
            left += 1

        return left
