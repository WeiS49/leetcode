#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
# Time: O(n)  Space: O(1)

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 设定首尾指针
        start, end = 0, len(numbers) - 1

        while start < end:

            left, right = numbers[start], numbers[end]
            total = left + right
            # 比较total和target的大小, 确定左右指针移动
            if total < target:
                start += 1
            elif total > target:
                end -= 1
            else:
                return [start + 1, end + 1]
        



# @lc code=end

