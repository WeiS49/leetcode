#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
# 时间复杂度: O(mn), 循环嵌套, 运行时间与二维矩阵matrix中元素个数决定
# 空间复杂度: O(1), 使用常数次空间

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transposed = [[0] * m for _ in range(n)] # 因为是转置矩阵, 所以要相反
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed

# @lc code=end

















