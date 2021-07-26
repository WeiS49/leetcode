#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# 二分查找
# 时间复杂度: 单层循环, O(n)
# 空间复杂度: 占用常数个空间, O(1)

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        ans = 0
        temp = []
        while low <= high: # 选择范围缩小到只包含一个元素
            mid = (low + high) // 2

            
            # 题目要求向下取整, 所以优先处理<=的情况
            if mid * mid <= x: 
                # temp.append(mid)
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
            temp.append(mid)
        return ans
        # return temp


# @lc code=end

