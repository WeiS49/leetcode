#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# 借助辅助空间, 使用哈希表求解
# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 借助额外辅助空间, 哈希表长度与len(nums)相关, O(n)

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dicx = {}
        # 将数据保存至哈希表
        for i in nums:
            if i not in dicx.keys():
                dicx[i] = 1
            else:
                dicx[i] += 1
        
        # 遍历哈希表, 找到符合要求的数据
        for i in dicx.keys():
            if dicx[i] == 1:
                return i



# @lc code=end

