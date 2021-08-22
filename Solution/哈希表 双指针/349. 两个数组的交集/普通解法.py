#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# Time: O(n) 单层循环
# Space: O(1) 辅助空间是返回值, 不计入空间复杂度计算

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        def search(nums1, nums2, ans):
            for num in nums1:
                if num in nums2 and num not in ans:
                    ans.append(num)
        
        search(nums1, nums2, ans)

        return ans




# @lc code=end










