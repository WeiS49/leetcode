
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if node is None: continue
            if flag == 1:
                res.append(node.val)
            else:
                
                stack.append((0, node.right))
                stack.append((0, node.left))
                stack.append((1, node))

        return res
        