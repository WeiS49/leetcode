#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯

# 傻递归, 不做任何优化, 超时
# 时间复杂度: O(2^n)
# 空间复杂度: O(n)

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# @lc code=end

