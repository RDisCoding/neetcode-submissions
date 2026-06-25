# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        def dfs(root, ans):
            if not root: return
            ans.append(root.val)
            if root.right: 
                dfs(root.right, ans)
            else:
                dfs(root.left, ans)

            return ans
        
        res = [root.val]
        xl = []
        xr = []
        if root.left: 
            xl = dfs(root.left, [])
        if root.right: 
            xr = dfs(root.right, [])
        
        for i in range(len(xr)):
            res.append(xr[i])
        
        for j in range(len(xr), len(xl)):
            res.append(xl[j])
        
        return res
