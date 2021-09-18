#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组

# 滑动窗口
# 1. 初始化
# 2. 左右窗口
# 3. sumx累加nums[end]
# 4. 两个判断合并 - 赋值操作及左窗口移动
# 5. 返回值, 需要考虑特殊情况 - 不存在符合条件的子数组时, 返回0
# Time: O(n), Space: O(1)

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        import math

        min_len, sumx = math.inf, 0

        start = 0

        for end in range(len(nums)):
            sumx += nums[end]

            while sumx >= target:
                min_len = min(min_len, end - start + 1)
                sumx -= nums[start]
                start += 1
        
        return 0 if min_len == math.inf else min_len

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # total, left, right = 0, 0, 0
        # res = len(nums) + 1
        # while right < len(nums):
        #     total += nums[right]
        #     while total >= target:
        #         res = min(res, right - left + 1)
        #         total -= nums[left]
        #         left += 1
        #     right += 1
        # return res if res <= len(nums) else 0


# @lc code=end

