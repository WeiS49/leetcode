#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
# Time: O(n) Space: O(n)
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dicx = {}
        result = []
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            # 因为nums2[i] > stack[-1]的情况可能不止一个
            # 所以要用while而不是if
            # 测试用例nums2 = [6,5,4,3,2,1,7]
            while stack and nums2[i] > stack[-1]:
                dicx[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        for element in stack:
            dicx[element] = -1
        
        for i in nums1:
            result.append(dicx[i])
        
        return result



# @lc code=end

