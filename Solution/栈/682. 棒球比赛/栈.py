#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
# Time: O(n), 执行次数为len(ops)
# Space: O(n), 辅助空间长度为len(ops)

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        s = 0
        for i in ops:

            if i == "C":
                s -= stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
                s += stack[-1]
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
                s += stack[-1]
            else:
                stack.append(int(i))
                s += stack[-1]
        return s


# @lc code=end

