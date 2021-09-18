#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找

# 普通的二分查找, 有一些细节值得注意
# Time: 单层循环, O(n)
# Space: 常量, O(1)

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target not in nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:

            # 改进: mid = low + (high - low) // 2, 预防溢出的情况
            mid = (low + high) // 2

            # 改进: 增加了额外的判断, 找到了就返回值而不用一致执行到底, 减少执行次数
            # if target == nums[mid]:
                # return mid 

            if target <= nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
                
        return low




# @lc code=end

