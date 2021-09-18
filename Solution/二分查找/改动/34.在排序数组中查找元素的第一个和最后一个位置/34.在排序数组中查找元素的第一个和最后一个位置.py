
# @lc app=leetcode.cn id=34 lang=python3
# [34] 在排序数组中查找元素的第一个和最后一个位置
# 用两次单独的二分查找来分别找起始点和结束点
# 时间复杂度: 二分查找, O(2logn) = O(logn)
# 空间复杂度: 只保存了常数个的指针, 不随数组大小而变化, O(1)

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid # 超出范围
            else:
                l = mid + 1 # 不在范围内
        start = l
        
        if not nums or nums[start] != target:
            return [-1, -1]

        r = len(nums) - 1 # 注意数组长度应该-1
        while l < r:
            mid = (l + r + 1) // 2 # 这里的+1可以规避掉无限循环
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        end = r
        return [start, end]
# 这种解法不太严谨, 如果可以还是应该单独写nums[mid] == target的情况

























        # # 取起始下标
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = (l + r) // 2
        #     if nums[mid] >= target:
        #         r = mid
        #     else:
        #         l = mid + 1
        # start = l
        
        # # 没找到
        # if not nums or nums[l] != target:
        #     return [-1,-1]
        
        # # 取结束下标
        # r = len(nums) - 1
        # while l < r:
        #     mid = (l + r + 1) // 2
        #     if nums[mid] <= target:
        #         l = mid
        #     else:
        #         r = mid - 1
        # end = r
        
        # return [start, end]




# @lc code=end

