#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
# 在创建栈stack的同时同步维护一个栈min_stack, 用来保存最小值, 弹出操作与stack同步
# 时间复杂度, 各项操作均为O(1)
# 空间复杂度, 最差时可能要同时添加两个栈的内容, O(2n) = O(n)

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

