# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0 
        def dfs(node, max_node):
            nonlocal ans
            if node == None:
                return 
            if node.val >= max_node:
                max_node = node.val
                ans += 1

            left = dfs(node.left, max_node)
            right = dfs(node.right, max_node)

        dfs(root, root.val)
        return ans

