#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
# Time: O(n) 单层循环
# Space: O(1) 常数次空间

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 正向思维, 相对容易考虑
        # dp保留这一级的最小消耗
        # 正着思考这道题, 每次到达就计算cost
        # dp[i] = 这一级的cost + min(上一级的cost, 上上级的cost)
        length = len(cost)
        dp = [0] * length
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, length):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[-1], dp[-2])


# @lc code=end

