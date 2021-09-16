#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
# 1. 声明初始值 - 最大长度(返回值)max_len、存储结果hashMap 
# 2. 设置左边界start=0, 右边界从0开始循环递增
# 3. 将遍历结果存储至哈希表, 若此时长度<=k(说明可以接受), 赋值操作
# 4. 因为窗口长度不固定, 可能执行多次, 所以使用while, 左侧移动
# 5. 返回结果max_len
# Time: O(n) - 最多执行n次, 无视循环嵌套
# Space: O(n) - 使用哈希表存储结果

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len, hashMap = 0, {}

        start = 0
        for end in range(len(nums)):
            tail = nums[end]
            hashMap[tail] = hashMap.get(tail, 0) + 1

            if hashMap.get(0, 0) <= k:
                max_len = max(max_len, end - start + 1)

            while hashMap.get(0, 0) > k:
                head = nums[start]
                hashMap[head] -= 1
                start += 1
                
        return max_len


# @lc code=end

