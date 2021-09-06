#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# 直接使用列表去模拟结果可能会报错
# 因为操作逻辑不同
# 所以选择在每次push数值的时候都重新调整列表的数字排序
# 使其符合一个队列的特性, 按照队列操作即可

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # self.queue.append(x)
        # for _ in range(len(self.queue) - 1):
        #     self.queue.append(self.queue.pop(0))
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.pop(0))
        # self.queue.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # return self.queue.pop(0)
        return self.queue.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        # return self.queue[0]
        return self.queue[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.queue) == 0 else False




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

