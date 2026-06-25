# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            lm = dfs(root.left)
            rm = dfs(root.right)

            total = root.val + max(lm,0) + max(rm,0)

            res[0] = max(res[0], total)

            return root.val + max(max(lm, 0), max(rm,0))
        
        dfs(root)

        return res[0]