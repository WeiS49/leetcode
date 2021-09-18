#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# Time: O(m * n) m, n分别为给定的行、列数
# Space: O(m * n) 需要创建一个二位数组保存所有结果

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 根据给定的行、列创建二维数组
        s = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                # 根据递推式获取结果
                # 类似于爬楼梯, 只不过是将走1、2格变成了向左、向右
                s[i][j] = s[i-1][j] + s[i][j-1]

        return s[-1][-1]
        


# @lc code=end

