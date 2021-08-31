#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
# 先计算其他位的结果, 最后单独处理最后一位
# Time: O(n) Space: O(1)
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 算是题目给出的条件, 不计入空间复杂度
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        length = len(s)
        for i in range(1, length):
            if roman[s[i-1]] >= roman[s[i]]:
                ans += roman[s[i-1]]
            elif roman[s[i-1]] < roman[s[i]]:
                ans -= roman[s[i-1]]
        ans += roman[s[-1]]
        return ans







# @lc code=end

