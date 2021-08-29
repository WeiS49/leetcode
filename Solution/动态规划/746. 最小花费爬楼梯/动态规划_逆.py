#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
# Time: O(n) 单层循环
# Space: O(n) 辅助空间长度为给定数组长度

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 这里dp保存的是从到达第i格消耗的最佳cost
        # 题目规定可以走1、2格
        # 根据题意判断, 从起点出发不消耗cost
        # 所以从起点开始, 能够到达第0格, 第1格, 所以dp[0] == dp[1] == 0
        dp = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            # 从第i格出发消耗的cost == 到达这格的cost + 移动消耗的cost
            # 即为dp[i] + cost[i]
            # 为了到达第i格, 可以走1、2格, 且需要找到它的最小值
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]

# @lc code=end

