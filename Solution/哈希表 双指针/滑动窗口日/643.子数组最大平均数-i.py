#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I

# 1. 创建初始值: 最大总和sum_, 最大平均数(返回值)ans
# 2. 定义左边界start=0, 右边界从0开始循环递增
# 3. 滑动窗口长度 == 最大长度k: 执行比较赋值操作
# 4. 若窗口达到上限, 左边界移动
# 5. 返回ans

# Time: O(n)
# Space: O(1)

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_, ans = 0, -float("inf")
        start = 0
        for end in range(len(nums)):
            sum_ += nums[end]
            
            if end - start + 1 == k:
                ans = max(ans, sum_ / k)

            if end - start + 1 >= k:
                sum_ -= nums[start]
                start += 1

        return ans

# @lc code=end

