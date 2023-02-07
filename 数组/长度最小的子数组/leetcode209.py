"""
    给定一个含有 n 个正整数的数组和一个正整数 target 。
    找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0
"""

# 解法1 ：滑动窗口法
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = 1e5 + 1
        result = 0
        i = 0
        for j in range(len(nums)):
            result += nums[j]
            while result >= target:
                length = min(length, j-i+1)
                result -= nums[i]
                i += 1
        return 0 if length == 1e5+1 else length