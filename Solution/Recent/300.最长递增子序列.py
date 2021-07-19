#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# 时间复杂度: 双层循环嵌套, O(n^2)
# 空间复杂度: 辅助空间为单个列表, 列表长度与给定列表nums有关, O(n)

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        length = len(nums)
        # 这种写法借鉴了第246题的代码, 初始化语句的不同可能会影响后续代码操作简便程度
        # 这种写法的空间复杂度更小(后者是超过6-8%, 这种写法超过了94%)
        dp = [1] * length 
        # dp = [] # 两种写法等效, 这种要写两句: 16行和18行
        for i in range(length):
            # dp.append(1) # 可能与append有关?
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # 这里+1是因为
        # return max(dp)
        return dp




# @lc code=end

