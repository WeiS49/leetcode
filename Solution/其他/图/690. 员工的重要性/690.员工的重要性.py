#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# 先遍历一遍给定的字典, 将其中id作为key
# 开始递归, 遍历子员工, 分别加上其对应下属的importance

# Time: O(n) 遍历所有员工
# Space: O(n) 借用辅助空间保存员工信息

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        dicx = {}
        for emp in employees:
            dicx[emp.id] = emp
        
        def dfs(id):
            emp = dicx[id]
            importance = emp.importance
            for e in emp.subordinates:
                importance += dfs(e)
            return importance
        return dfs(id)
    










# @lc code=end

