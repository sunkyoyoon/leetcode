# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {v:i for i, v in enumerate(inorder)}

        def dfs(inL, inR, poL, poR):
            if inL > inR:
                return 
            root_val = postorder[poR]
            root = TreeNode(root_val)

            mid = idx[root_val]
            length = mid - inL

            root.left = dfs(
                inL, mid - 1,
                poL, poL + length - 1
            )

            root.right = dfs(
                mid + 1, inR,
                poL + length, poR - 1
            )

            return root 


        return dfs(0, len(inorder)-1, 0, len(postorder)-1)
        
