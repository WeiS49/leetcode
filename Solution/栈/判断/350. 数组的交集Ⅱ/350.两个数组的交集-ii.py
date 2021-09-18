#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
# @lc code=start

# 哈希表
# Time: O(n) Space: O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        dicx = {}
        ans = []
        # 遍历更小的数组, 将出现次数添加到哈希表中
        for i in range(len(nums1)): 
            num = nums1[i]
            if nums1[i] not in dicx.keys():
                dicx[num] = 1
            else:
                dicx[num] += 1
        # 数值在哈希表中出现, 添加并次数-1
        for i in range(len(nums2)):
            num = nums2[i]
            if num in dicx.keys():
                if dicx[num] == 0:
                    pass
                else:
                    ans.append(num)
                    dicx[num] -= 1
        return ans
        





# @lc code=end

