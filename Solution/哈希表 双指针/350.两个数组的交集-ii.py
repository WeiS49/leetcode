#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
# 双指针
# Time: O(nlogn) Space: O(n)
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 对两个数组进行排序
        nums1.sort()
        nums2.sort()
        # 设定索引
        index1, index2 = 0, 0
        length1, length2 = len(nums1), len(nums2)
        ans = []
        while index1 < length1 and index2 < length2:
            num1, num2 = nums1[index1], nums2[index2]
            # 符合条件就添加结果, 否则值相对较小的结果自增
            if num1 == num2:
                ans.append(num1)
                index1 += 1
                index2 += 1
            elif num1 < num2:
                index1 += 1
            else:
                index2 += 1

        return ans


# @lc code=end

