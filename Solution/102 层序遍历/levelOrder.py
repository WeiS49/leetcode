def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res

        # res = []
        # queue = [root]
        # while queue:
        #     level = []
        #     n = len(queue)
        #     for i in range(n):
        #         node = queue.pop(0)
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        #     res.append(level)

        return res