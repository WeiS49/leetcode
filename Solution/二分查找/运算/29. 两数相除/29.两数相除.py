#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# Time
# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        flag = 1
        # 如果输入值是负数, 则将其转化成整正数再操作
        if dividend < 0: flag, dividend = -flag, -dividend
        if divisor < 0: flag, divisor = -flag, -divisor

        res = 0

        while dividend >= divisor:
            cur = divisor
            time = 1
            while cur + cur < dividend:
                cur += cur
                time += time
            dividend -= cur
            res += time
        
        res = res if flag == 1 else -res
        if res < MIN_INT:
            return MIN_INT
        elif res > MAX_INT:
            return MAX_INT
        else:
            return res

# @lc code=end

