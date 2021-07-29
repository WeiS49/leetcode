#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串

# 特解 - 使用切片
# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 
#   解法1: 最后的比较中使用了切片, O(n), n为new_s长度
#   解法2: 额外占用了常量个数的变脸, O(1)

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        # 想办法从给定字符串中提取数字和字母
        for w in s:
            if w.isalnum():
                new_s += w.lower()

        # 解法1 - 使用切片比较是正序和倒序是否一致
        # return new_s == new_s[::-1]

        # 解法2 - 双指针
        start = 0
        end = len(new_s) - 1
        while start <= end:
            # 不一致则返回False
            if new_s[start] != new_s[end]:
                return False
            start, end = start + 1, end - 1
        return True










# @lc code=end

