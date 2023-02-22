"""
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
    假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
    可以按任意顺序返回答案。
"""

# 解法一：暴力遍历
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
            i += 1

# 解法二：字典形式实现
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for index, value in enumerate(nums):
            if target - value in result:
                return [result[target-value], index]
            result[value] = index
        return []