# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return (0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            curr = node.val + left[0] + right[0]
            return (max(left) + max(right), curr)

        return max(dfs(root))
