#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
# Time: O(n)  Space: O(n)
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        length = len(s)
        # 初始化dp函数
        # dp[i]表示当前元素是否可以"使用"
        dp = [False] * (length + 1)
        # dp[0]表示""的情况
        dp[0] = True
        # 两层循环遍历, 分别循环dp和s
        for i in range(length):
            for j in range(1, length + 1):
                # 若当前元素可以使用且能够构成s中的值
                if dp[i] and s[i:j] in wordDict:
                    # 执行操作
                    dp[j] = True
        return dp[-1]

# @lc code=end

