#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
# 改进的快速排序算法
# 时间复杂度: 最好情况为O(logn)
# 空间复杂度: 没有借助额外的辅助空间, 只有常数个变量, O(1)
# @lc code=start
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        target = length - k
        left = 0
        right = length - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1

    def __partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if pivot > nums[i]:
                j += 1
                nums[i], nums[j] = nums[j], nums[i] # 把循环中遇到的所有<pivot的值移动到pivot的左边
        nums[j], nums[left] = nums[left], nums[j]
        return j















    #     size = len(nums)

    #     target = size - k
    #     left = 0
    #     right = size - 1
    #     while True:
    #         index = self.__partition(nums, left, right)
    #         if index == target:
    #             return nums[index]
    #         elif index < target:
    #             # 下一轮在 [index + 1, right] 里找
    #             left = index + 1
    #         else:
    #             right = index - 1

    # #  循环不变量：[left + 1, j] < pivot
    # #  (j, i) >= pivot
    # def __partition(self, nums, left, right):

    #     pivot = nums[left]
    #     j = left
    #     for i in range(left + 1, right + 1):
    #         if nums[i] < pivot:
    #             j += 1
    #             nums[i], nums[j] = nums[j], nums[i]

    #     nums[left], nums[j] = nums[j], nums[left]
    #     return nums


# @lc code=end

