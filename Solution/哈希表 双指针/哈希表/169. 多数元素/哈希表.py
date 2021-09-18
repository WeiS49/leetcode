#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素

# 将所有元素及出现次数用哈希表保存, 返回value值最大的key值
# Time: O(n), Space: O(n)

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicx = {}
        for num in nums:
            if num in dicx.keys():
                dicx[num] += 1
            else:
                dicx[num] = 1
        return max(dicx, key=dicx.get)
        # current = 0
        # ans = 0
        # for k, v in dicx.items():
        #     if v > current:
        #         current = v
        #         ans = k
        # return ans



# @lc code=end

