
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:

            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        def helper(root):
            nonlocal res
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
            return res
        helper(root)
        return res
