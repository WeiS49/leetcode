#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
# 常见思路是构造一个容量为K的小顶堆, 堆顶即为所求
# 在数据量较大的情况下, 更优的解法
# 调用参数的解法
# Time: O(n)  Space: O(1)

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def findKth(low, high):
            pivot = random.randint(low, high)
            nums[pivot], nums[low] = nums[low], nums[pivot]
            base = nums[low]
            i, j = low, low + 1
            while j <= high:
                if nums[j] > base:
                    nums[j], nums[i+1] = nums[i+1], nums[j]
                    i += 1
                j += 1
            nums[i], nums[low] = nums[low], nums[i]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                return findKth(low, i - 1)
            else:
                return findKth(i + 1, high)
        return findKth(0, len(nums) - 1)
        



# @lc code=end

