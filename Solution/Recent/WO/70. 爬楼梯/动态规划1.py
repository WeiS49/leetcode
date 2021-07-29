#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯

# 动态规划, 没有用实际操作去运算f(n)=f(n-1)+f(n-2)
# 而是在找到逻辑后, 使用加法完成方法数量的计算

# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 占用空间随楼梯数n线性变化, O(n)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1) # 创建数组, 保存每一级的步数, 考虑到dp[0], 所以长度+1
        dp[0] = dp[1] = 1 # 为什么要设置dp[0]? 第0级楼梯吗
        for i in range(2, n + 1): # 从第2级到第n级楼梯开始使用递推式
            dp[i] = dp[i - 1] + dp[i - 2] # 用加法代替了递归的执行
        return dp[-1] # 返回数组中最后一个元素, 即为最终的方法数
# @lc code=end

