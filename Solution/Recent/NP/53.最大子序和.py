#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = nums[0], 0
        length = len(nums)
        for i in range(length):
            x = nums[i]
            if x > 0 :
                if current_sum <= 0:
                    current_sum = x
                else:
                    current_sum += x
            else:
                if current_sum > -x:
                    current_sum += x # 二者相加仍 > 0, 可以接受
                else:
                    current_sum = x # 二者相加 < 0, 重新赋初值

            if max_sum < current_sum:
                max_sum = current_sum

        return max_sum


# @lc code=end

