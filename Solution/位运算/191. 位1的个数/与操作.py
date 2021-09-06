#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
# 因为不论如何n(2) & n-1(2)都会少一位1
# 所以每进行一次, n(2)都会少一位1
# 因此, 计算执行"&"的次数即可计算出1的个数
# Time: O(n), Space: O(1)
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res


# @lc code=end

