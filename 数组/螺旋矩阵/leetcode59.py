"""
    给定一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[-1] * n for _ in range(n)]
        start_x, start_y, count = 0, 0, 1
        loop, mid = n // 2, n // 2
        for offset in range(1, loop+1):
            for i in range(start_y, n-offset):
                nums[start_x][i] = count
                count += 1
            for i in range(start_x, n-offset):
                nums[i][n-offset] = count
                count += 1
            for i in range(n-offset, start_y, -1):
                nums[n-offset][i] = count
                count += 1
            for i in range(n-offset, start_x, -1):
                nums[i][start_y] = count
                count += 1

            start_x += 1
            start_y += 1

        if n % 2 != 0:
            nums[mid][mid] = count

        return nums