#
# @lc app=leetcode.cn id=1695 lang=python3
#
# [1695] 删除子数组的最大得分
# 本质就是求最大连续不同元素的和
# 1. 初始化, 最大分数(返回值)max_score, 当前窗口内的值hashMap, 当前最大和sumx
# 2. 设定左右边界
# 3. 添加当前遍历值content至hashMap, 最大和累加content
# 4. 若当前长度==滑动窗口长度, 执行操作; 滑动窗口长度不确定 - while, 出现重复则左侧循环移动
# 5. 返回max_score
# Time: O(n) Space: O(n)
# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        max_score, hashMap, sumx = 0, {}, 0
        start = 0

        for end in range(len(nums)):
            content = nums[end]
            hashMap[content] = hashMap.get(content, 0) + 1
            sumx += content

            if len(hashMap) == end - start + 1:
                max_score = max(max_score, sumx)
            
            while end - start + 1 > len(hashMap):
                head = nums[start]
                hashMap[head] -= 1
                if hashMap[head] == 0:
                    del hashMap[head]
                sumx -= head
                start += 1
        
        return max_score


        #return max_score

# @lc code=end

