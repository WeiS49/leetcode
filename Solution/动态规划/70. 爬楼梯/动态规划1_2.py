#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯

# 动态规划的另一种写法, 不使用dp[0]去完成题目
# 符合现实逻辑(毕竟没有第0级楼梯), 但写起来麻烦(要添加限定条件: 考虑n=1的情况)

# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 占用空间随楼梯数n线性变化, O(n)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: # 如果不使用dp[0], 就要添加限定条件
            return n
        dp = [0] * (n + 1) # 因为索引是从0开始的, 所以创建n+1个元素
        dp[1], dp[2] = 1, 2 # 这算是题干给出的条件, 不考虑dp[0]的情况
        for i in range(3, n + 1): # 直接从第3级开始
            dp[i] = dp[i-1] + dp[i-2] # 套用递推式, 用加法规避递归计算
        return dp[-1]

# @lc code=end

