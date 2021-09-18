#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicx = {}
        for num in nums:
            # 在dicx中查找num的值, 若num不存在则返回0(int)
            dicx[num] = dicx.get(num,0) + 1
        for k, v in dicx.items():
            if v == 1:
                return k
# @lc code=end

