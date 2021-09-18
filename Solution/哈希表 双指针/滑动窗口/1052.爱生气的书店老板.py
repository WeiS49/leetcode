#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
# 乍一看很复杂, 实际上是很基础的滑动窗口
# 1. 设定初值 - 不生气时顾客sumx, 生气时顾客sumy, 技能揽客extra
# 2. 设定左右边界 - start=0, end=0循环递增, 长度为开张时间
# 3. 根据生气与否对sumx, sumy进行累加. 
# 4. 窗口长度k == 技能持续minutes -> 赋值操作; k > minutes -> 左窗口移动
# 5. 返回sumx + extra, 意为不生气顾客数 + 技能揽客数
# Time: O(n) Space: O(1)

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        sumx, sumy = 0, 0
        extra = 0
        start = 0
        for end in range(len(customers)):
            if grumpy[end] == 0:
                sumx += customers[end]
                customers[end] = 0
            elif grumpy[end] == 1:
                sumy += customers[end]

            if end - start + 1 == minutes:
                extra = max(extra, sumy)

            if end >= minutes - 1: 
                sumy -= customers[start]
                start += 1
            
        return sumx + extra


        # start = 0
        # extra = 0
        # for end in range(len(customers)):
        #     sum_.append(customers[end])
            
        #     if len(sum_) == minutes:
        #         extra = max(extra, sum(customers))
            
        #     if len(sum_) > minutes:
        #         sum_.pop()
        #         start += 1
        
        # return sumx + extra
        


# @lc code=end

