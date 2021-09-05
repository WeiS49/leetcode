#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
# 模拟加法
# Time: O(n), Space: O(n)
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, res = a[::-1], b[::-1], []
        i, j, carry = 0, 0, 0
        while i < len(a) or j < len(b) or carry:
            n1 = int(a[i]) if i < len(a) else 0
            n2 = int(b[j]) if j < len(b) else 0
            ans = n1 + n2 + carry
            carry = ans // 2
            ans %= 2
            res.append(str(ans))
            i, j = i + 1, j + 1
            
        return "".join(res[::-1])

# @lc code=end

