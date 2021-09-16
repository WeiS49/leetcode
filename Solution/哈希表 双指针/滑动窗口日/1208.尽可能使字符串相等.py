#
# @lc app=leetcode.cn id=1208 lang=python3
#
# [1208] 尽可能使字符串相等
# 1. 赋初值, 最大长度max_len
# 2. 设定左右边界 - 左侧从0开始, 右侧从从0开始递增(注意ASCII码计算)
# 3. 计算开销范围, 如果可以接受, 则执行赋值操作
# 4. 窗口长度不固定 - while. 若超出预算, 左侧循环移动
# 5. 返回max_len
# Time: O(n) Space: O(1)
# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        max_len, cur = 0, 0

        start = 0
        for end in range(len(t)):

            cur += abs(ord(t[end]) - ord(s[end]))
            if cur <= maxCost:
                max_len = max(max_len, end - start + 1)
            
            while cur > maxCost:
                cur -= abs(ord(t[start]) - ord(s[start]))
                start += 1

        return max_len

# @lc code=end

