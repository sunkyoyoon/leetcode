# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for i, v in enumerate(postorder):
            hashmap[v] = i 
        
        def dfs(pre_l, pre_r, post_l, post_r):
            if pre_l > pre_r:
                return 
            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            if pre_l == pre_r:
                return root

            idx = preorder[pre_l+1]

            mid = hashmap[idx]

            length = mid - post_l + 1 

            root.left = dfs(pre_l+1, pre_l + length, post_l, mid)
            root.right = dfs(pre_l+length+1, pre_r, mid+1, post_r-1)

            return root


        return dfs(0, len(preorder)-1, 0, len(postorder)-1)
