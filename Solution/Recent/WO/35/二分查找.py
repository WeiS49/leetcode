#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# 二分查找, 关注while条件, if target not in nums: 要求返回 第一个 比它大的下标
# 时间复杂度: 二分查找, O(logn)
# 空间复杂度: 使用常量空间, O(1)

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if nums[r] < target:
            return len(nums)
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target: # 这可以少执行常数步
                return mid
            else:
                r = mid - 1

        return l



        # length = len(nums)
        # l, r = 0, length - 1
        # if nums[r] < target:
        #     return length
        # while l <= r: 
        #     mid = (l + r) // 2
        #     if nums[mid] < target: # 根据题意, 优先考虑右区间 
        #         l = mid + 1 # l和r是否+1需要结合题意考虑(第一个/最后一个)
        #     else:
        #         r = mid - 1
        # return l





        # length = len(nums)
        # l, r = 0, length - 1
        # if nums[r] < target:
        #     return length
        # while l < r: 
        #     mid = (l + r) // 2
        #     if nums[mid] < target: # 根据题意, 优先考虑右区间 
        #         l = mid + 1 # l和r是否+1需要结合题意考虑(第一个/最后一个)
        #     else:
        #         r = mid
        # return l
# @lc code=end

