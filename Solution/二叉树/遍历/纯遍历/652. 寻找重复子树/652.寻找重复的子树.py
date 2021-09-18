#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历所有路径的题目
# 首先应该明确需要使用遍历的顺序, 然后想怎么创建符合要求的结果
# 接下来是想好条件, 每次执行语句都判断是否满足条件
# 将符合条件的结果保存即可.
# 用字典保存每一位的中间值, 如果符合要求, 将节点添加进res中

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        if not root:
            return []

        self.res = []
        self.dicx = {}

        self.inorder(root)
        return self.res

        
    def inorder(self, root):

        if root:
            ls = str(root.val) + "-" + self.inorder(root.left) + "-" + self.inorder(root.right)
            count = self.dicx.get(ls, 0)
            if count == 1:
                self.res.append(root)
            self.dicx[ls] = count +1

            return ls

        else:
            return "#"









# @lc code=end

