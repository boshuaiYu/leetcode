"""
    编写一个算法来判断一个数 n 是不是快乐数。

    「快乐数」 定义为：
        1. 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
        2. 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
        3. 如果这个过程 结果为 1，那么这个数就是快乐数。
    如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        def cal(num):
            sum = 0
            while num:
                sum += (num % 10) ** 2
                num = num // 10
            return sum

        val = set()

        while True:
            n = cal(n)
            if n == 1:
                return True
            if n in val:
                return False
            else:
                val.add(n)

# set与dict的区别参考：https://blog.csdn.net/weixin_42782150/article/details/122171083
# 集合和字典基本相同，唯一的区别，就是集合没有键和值的配对，是一系列无序的、唯一的元素组合。(集合只有键，字典有键值对)
