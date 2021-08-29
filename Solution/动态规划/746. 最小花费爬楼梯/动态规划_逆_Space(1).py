#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
# Time: O(n) 单层循环
# Space: O(1) 常数次空间

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 同理, 也可以用两个"指针"代替dp(list)的操作, 让空间复杂度变为O(1)
        prev, curr = 0, 0
        for i in range(2, len(cost) + 1):
            nxt = min(prev + cost[i-2], curr + cost[i-1])
            prev, curr = curr, nxt
        return curr


# @lc code=end

