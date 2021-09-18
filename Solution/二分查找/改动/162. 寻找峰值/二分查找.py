#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
# 四种情况, 分成两类
# 1. 两端为峰值
#   1. nums单调递增(右大)
#   2. nums单调递减(左大)
# 2. 中间为峰值(二分查找mid值)
#   1. mid+1 > mid or mid-1 > mid:
#       说明峰值在更大的一侧, 设为x
#           若x先增后减 —— mid+1即为峰值
#           若x先减后增 —— 回到第一种情况
#   2. mid > mid+1 && mid > mid-1
#       return mid
# 关键就是要意识到, 哪边比mid值大, 哪边就更有可能出现峰值
# Time: O(n), Space: O(1)

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        # left == right时不能再执行, 否则可能会溢出
        # 以为这道题是需要调用[mid+1] 和 [mid-1], 所以要考虑
        while left < right: 
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left += 1
            else:
                right -= 1
        
        return left if nums[left] > nums[right] else right
            





# @lc code=end

