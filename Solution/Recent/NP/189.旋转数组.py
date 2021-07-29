#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 使用了额外的辅助空间, 大小与n和k相关, O(n-k) = O(n)


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1



# @lc code=end

