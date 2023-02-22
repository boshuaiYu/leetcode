"""
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
    注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
"""


# 解法一：数组遍历，数组本身实现就是哈希表代表
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list = [0] * 26
        for i in s:
            list[ord(i) - ord("a")] += 1
        for i in t:
            list[ord(i) - ord("a")] -= 1
        for i in range(26):
            if list[i] != 0:
                return False
        return True


# 以下方法雕鹰collections的库
# 具体相关可以参考：https://docs.python.org/zh-cn/3/library/collections.html#module-collections

# 解法二：使用defaultdict的方法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict


# 解法三：使用Counter的方法
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_counter = Counter(s)
        t_counter = Counter(t)
        return a_counter == t_counter
