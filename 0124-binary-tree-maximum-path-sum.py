        ans = float("-inf")

        def dfs(node):
            nonlocal ans
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # best path that passes through this node
            ans = max(ans, node.val + left + right)

            # best path going upward (one side only)
            return node.val + max(left, right)

        dfs(root)
        return ans
