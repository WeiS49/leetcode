#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
# 无脑解法, 思路就是从数组中取出再进行操作
# Time: O(n * nlogn) 排序嵌套循环
# Space: O(1), 在原数组中进行操作, 不涉及其他辅助空间

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) == 1:
                return stones[-1]
            stones.sort()
            stone2, stone1 = stones.pop(), stones.pop()
            if stone1 == stone2:
                if len(stones) == 0:
                    return 0
                continue
            else:
                left = stone2 - stone1
                stones.append(left)
            



# @lc code=end

