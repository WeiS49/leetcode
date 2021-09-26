#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy, sell = -float("inf"), 0

        for p in prices:
            buy = max(buy, -p)
            sell = max(sell, buy + p)
        
        return sell

# @lc code=end

