#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1


        
# @lc code=end

