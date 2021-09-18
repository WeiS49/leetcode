#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
# 这道题可以转换为滑动窗口 - 找到拿取的最大点数(求解) == 找到不拿的最小点数(滑动窗口)
# 1. 初始化 - 当前最小值sumx, 滑动窗口长度windows, 最小点数(返回值)min_point
# 2. 设定左右边界: start=0, end=0循环递增
# 3. 计入当前结果cardPoints[end], 若当前滑动窗口长度==实际滑动窗口长度windows -> 执行操作
# 4. 若此时长度达到要求(滑动窗口长度) - 左侧移动
# 5. 通过总和-不拿最小点数 -> 拿取的最大点数, 排除特殊情况(全拿)
# Time: O(n) Space: O(1)

# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        sumx = 0
        windows = len(cardPoints) - k
        min_point = float("inf")

        start = 0
        for end in range(len(cardPoints)):
            sumx += cardPoints[end]
            if end - start + 1 == windows:
                min_point = min(min_point, sumx)
            
            if end >= windows - 1:
                sumx -= cardPoints[start]
                start += 1
        
        return sum(cardPoints) if min_point == float("inf") else sum(cardPoints) - min_point


# @lc code=end





