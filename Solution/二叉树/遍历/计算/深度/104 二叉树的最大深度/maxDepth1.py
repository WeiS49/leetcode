class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0    # 递归结束, 最终会返回0
        else:
            return max(map(self.maxDepth, (root.left, root.right))) + 1 # 每进行一次递归, 都相当于深度+1

# 展开写法
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        length = max(left, right)
        return length + 1            