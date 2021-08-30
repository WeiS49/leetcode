#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
# Time: O(nlogn) - 循环嵌套;  Space: O(1)

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 通过循环确定第一个数字, 第二个数字通过标准的二分查找获取
        for i in range(len(numbers)):
            index = i + 1
            left, right = index, len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                num = numbers[mid]
                total = num + numbers[i]
                if total < target:
                    left = mid + 1
                elif total > target:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]
        return [-1, -1]



# @lc code=end

