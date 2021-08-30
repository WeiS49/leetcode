#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加

# 将字符串转换成ASCII码进行操作, 然后再转回字符串
# Time: O(n), Space: O(1)

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 首先根据给定字符串的长度找到索引, 注意下标从0开始/
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0 # 默认的进位是0
        res = ""
        while i >= 0 or j >= 0: # 当二者有任意不为空, 进行加法
            # 如果位数不足则用"0"替代
            n1 = num1[i] if i >= 0 else "0"
            n2 = num2[j] if j >= 0 else "0"
            # ASCII码加法
            tmp = ord(n1) + ord(n2) - 2 * ord("0") + carry
            carry = tmp // 10 # 获取进位
            ans = tmp % 10 # 获取结果
            res = chr(ans + 48) + res # 转换回字符串形式

            i -= 1
            j -= 1

        return res if not carry else "1" + res

# @lc code=end

