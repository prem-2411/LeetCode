class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.insert(0, level)

        return result