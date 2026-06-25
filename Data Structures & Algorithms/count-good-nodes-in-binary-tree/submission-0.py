# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        current = float('-inf')
        def dfs(root, current):
            nonlocal ans
            if not root: return 
            if root.val >= current:
                current = root.val 
                ans+=1
            dfs(root.left, current)
            dfs(root.right, current)
        
        dfs(root, current)
        return ans