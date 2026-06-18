# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.m = float('-inf')
        def maxSum(root): #20
            if not root: 
                return 0
            
            leftMax = max(maxSum(root.left), 0)
            rightMax = max(maxSum(root.right), 0)

            total = root.val + leftMax + rightMax #50
            self.m = max(self.m, total)

            return root.val + max(leftMax, rightMax)
        
        maxSum(root)
        return self.m

