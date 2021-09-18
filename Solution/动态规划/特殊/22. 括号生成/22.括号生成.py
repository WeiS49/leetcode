#
# @lc app=leetcode.cn id=22 lang=python3
#

# @lc code=start
# [22] 括号生成
# 分为三层, total_l -> l -> str
# Time: O(n^4)???  Space: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: # 排除特殊情况
            return []
        # 动态规划对dp做初始化
        total_l = [[""], ["()"]]

        for i in range(2, n + 1):
            l = []  # 对单层列表做初始化
            for j in range(i):
                list1, list2 = total_l[j], total_l[i-j-1]
                for k1 in list1:
                    for k2 in list2:
                        res = "(" + k1 + ")" + k2
                        l.append(res)
            total_l.append(l)
        return total_l[-1]


# @lc code=end

