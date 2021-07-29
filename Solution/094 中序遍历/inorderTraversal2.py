
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        White, Gray = 0, 1
        res = []
        stack = [(White, root)]

        while stack:

            color, node = stack.pop()
            if node is None:
                continue
            if color == White:
                stack.append((White, node.right))
                stack.append((Gray, node))
                stack.append((White, node.left))
            else:
                res.append(node.val)
        return res


        
