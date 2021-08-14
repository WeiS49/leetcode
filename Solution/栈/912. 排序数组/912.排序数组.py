#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
# 
# 快速排序
# 时间复杂度: 平均复杂度为O(nlogn)
# 空间复杂度: 取决于递归的深度, 最差为O(n)

# @lc code=start
class Solution:
    
    def sortArray(self, nums: List[int]) -> List[int]:
        less = []
        great = []
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[len(nums) // 2] # 建议随机pivot
            nums.remove(pivot)
            for num in nums:
                if num < pivot:
                    less.append(num)
                else:
                    great.append(num)
            return self.sortArray(less) + [pivot] + self.sortArray(great)

# @lc code=end

