#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# 无脑解法, 添加进去后删除0
# 需要增补其他解法
# Time: O(n)
# Space: O(n)

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        for i in range(len(nums2)):
            nums1.remove(0)



# @lc code=end

