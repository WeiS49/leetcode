#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
# 还是一道二维爬楼梯, 只是要计算总和而不是可能性
# 因为某一位置只能从其上或其做到达
# 所以 路径值 = 当前路径值 + min(上, 左)
# 两种思路:
# 1. 额外创建一个二维数组, 用来保存所有路径 ×
# 2. 直接使用对原数组进行操作, 返回最终路径 √

# Time: O(n^2) Space: O(1)
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

        # m, n = len(grid), len(grid[0])
        # path = [[0] * n for _ in range(m)]
        # path[0][0] = grid[0][0]
        # for i in range(1, n):
        #     path[0][i] = grid[0][i]
        # for i in range(1, m):
        #     path[i][0] = grid[i][0]

        # for i in range(1, n):
        #     path[0][i] += path[0][i-1]
        # for i in range(1, m):
        #     path[i][0] += path[i-1][0]
    
        # for i in range(1, m):
        #     for j in range(1, n):
        #         path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]

        # return path

        # for i in range(1, n):
        #     grid[0][i] += grid[0][i-1]
        # for i in range(1, m):
        #     grid[i][0] += grid[i-1][0]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        # return grid[-1][-1]






# @lc code=end

