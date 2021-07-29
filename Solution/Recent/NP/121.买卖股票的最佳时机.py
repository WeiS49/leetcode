#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# 暴力解法
# 时间复杂度: 循环嵌套, 所以复杂度为O(n^2)
# 空间复杂度: 只用到常数个变量, 常数空间复杂度O(1)
# 但似乎这样做会超时, 所以还是用作加深印象吧

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # current_profit = float("inf")
        # min_price = 0
        # profit = 0
        # length = len(prices)
        # for i in range(length):
        #     for j in range(i + 1, length):
                # current_profit = prices[j] - prices[i]
                # if current_profit > profit:
                #     profit = current_profit
                # profit = max(profit, prices[j] - prices[i])

        # return profit











        inf = float("inf")
        profit = 0
        min_price = inf
        for price in prices:
            profit = max(price - min_price, profit)
            min_price = min(price, min_price)
        return profit











        # dp0 = 0
        # dp1 = -prices[0]
        # dp2 = -float("inf")

        # for price in prices:
        #     dp1 = max(dp0 - price, dp1) # 比较当前最低买入价和历史最低买入价哪个小, 更新数据
        #     dp2 = max(dp1 + price, dp2) # 比较当前利润和历史最高利润哪个大, 更新数据

        # return max(dp2, dp0)









# @lc code=end

