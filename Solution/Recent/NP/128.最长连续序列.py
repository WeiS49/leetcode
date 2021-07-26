#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列

# 动态规划解法
# 时间复杂度: 单次循环, O(n)
# 空间复杂度: 占用空间只随提供的数组大小而定, 其他变量均为常数次, O(n)

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 # 保存当前最大值的变量
        dicx = {}
        
        for num in nums:
            if num not in dicx:
                left = dicx.get(num - 1, 0) # 获取num值左侧的序列长度(没有则为0)
                right = dicx.get(num + 1, 0) # 右侧
                current_length = left + 1 + right

                if current_length > res:
                    res = current_length # 如果出现最大的

                dicx[num] = 1 # 中间点功能是占位, 不作实际用途, 如有需要后面会重新赋值
                dicx[num - left] = current_length # 关键时刻延伸的左右端点(遗漏)
                dicx[num + right] = current_length

        return res























        # for num in nums:
        #     if num not in dicx:
        #         left = dicx.get(num - 1, 0)
        #         right = dicx.get(num + 1, 0)
        #         current_length = left + 1 + right

        #         if current_length > max_length:
        #             max_length = current_length
            
        #         dicx[num] = current_length
        #         dicx[num-1] = current_length
        #         dicx[num+1] = current_length
        # return max_length




# @lc code=end

