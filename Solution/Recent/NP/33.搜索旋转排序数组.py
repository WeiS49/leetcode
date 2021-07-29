#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
# 二分查找
# 时间复杂度: O(log(2)n)
# 空间复杂度: 常数空间复杂度: O(1)
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums: # 特殊情况: 数组中没有内容
            return -1
        left, right = 0, len(nums) - 1 # 索引的起始和结束
        temp = []
        while left <= right:
            # 核心思路: 总是在有序的一边进行二分查找, 只要范围足够小, 总是能找到有序的子集
            # 和一般的二分查找相比, 这道题相当于加了一层判断: 该子集是否有序
            # 找到有序集合后, 判断target所在的区间: 有序集合内/有序集合外, 这一点同一般的二分查找一致
            # 普通的二分查找既可以写成: nums[mid] > target,也可以写成: nums[left] <= target < nums[mid]
            # 但这道题不行, 因为需要考虑到有序区间内进行操作, 只能写成后者
            mid = (left + right) // 2
            temp.append(mid)
            if nums[mid] == target: # 如果找到, 则直接返回索引(单独处理相等的情况)
                return mid
            if nums[left] <= nums[mid]: # 数组左半部分有序
                if nums[left] <= target < nums[mid]: # target在左半边(有序集合内)
                    right = mid - 1 # 向左缩小查找范围
                else: # target在右半边
                    left = mid + 1 # 向右缩小查找范围
            else: # 数组右半部分有序
                if nums[mid] < target <= nums[right]: # 注意等号, 少了等号的那一侧是因为等号被单独处理了
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        # return temp

# @lc code=end

