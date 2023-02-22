"""
    给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。
"""


# 解法一：通过字典方法
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        val = {}
        list = []
        for num in nums1:
            val[num] = 1
        for num in nums2:
            if num in val.keys() and val[num] == 1:
                list.append(num)
                val[num] = 0
        return list


# 解法二：通过字典特殊的求并集操作
# 参考：https://blog.csdn.net/qq_43328040/article/details/106592596
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = set(nums1)
        list2 = set(nums2)
        return list(list1 & list2)
# 注意list，set，dict时是不可哈希的，可以遍历后再哈希
