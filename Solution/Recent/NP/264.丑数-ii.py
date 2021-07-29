#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# 堆 + 动态规划
# 时间复杂度: 单次循环, 复杂度为O(n)
# 空间复杂度: 占用空间大小随输入值n的大小而定, 指针为常数次, 复杂度为O(n)


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1) # 根据输入值n确定列表长度(返回第n个, 列表长度设为n+1)
        dp[1] = 1 # 跳过dp[0], 这样便于之后的返回值
        p2, p3, p5 = 1, 1, 1 # 声明三个指针, 赋初始值为1(代表一倍)
        for i in range(2, n + 1):
            num2, num3, num5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(num2, num3, num5) # 取3个值中的最小, 对列表中的值重新赋值
            if dp[i] == num2: # 如果相等, 说明该值已被添加进列表, 指针指向进位, 指向下一个数即可
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        return dp[n]


# @lc code=end

