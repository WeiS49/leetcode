#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for i in s:
            if i in hashMap.values(): # 检索value值, 也就是括号的左半部分
                stack.append(i)
            elif i in hashMap.keys():
                if not stack:   # 一定要优先进行特殊情况操作
                    return False
                if hashMap[i] != stack.pop() : # 
                    return False
            else:
                return False

        return stack == []





# @lc code=end

