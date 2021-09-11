#

# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
# 常见思路是构造一个容量为K的小顶堆, 堆顶即为所求
# 在数据量较大的情况下, 更优的解法
# 调用参数的解法
# Time: O(nlogk)  Space: O(logk)

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]



# @lc code=end

