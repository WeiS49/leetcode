#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        index1, index2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        ans = []
        
        while index1 < length1 and index2 < length2:
            num1 = nums1[index1]
            num2 = nums2[index2]

            if num1 == num2:
                if num1 not in ans:
                    ans.append(num1)
                index1 += 1
                index2 += 1
            elif num1 > num2:
                index2 += 1
            else:
                index1 += 1

        return ans



# @lc code=end

