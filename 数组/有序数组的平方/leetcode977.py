"""
给定一个按非递减顺序排序的整数数组 nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序
"""

# 解法1：暴力平方排序法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            nums.sort()
        return nums

# 解法2：双指针法
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        length = len(nums)
        left, right, k = 0, length - 1, length - 1
        result = [-1] * length
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result[k] = nums[left] ** 2
                left += 1
            else:
                result[k] = nums[right] ** 2
                right -= 1
            k -= 1

        return result
