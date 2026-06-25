# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = root
        
        def checkLeaf(root):
            if not root.left and not root.right: 
                return True
            else:
                return False

        def dfs(root, val):
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                else:
                    dfs(root.left, val) 
            elif val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                else:
                    dfs(root.right, val)

        if not root:
            return TreeNode(val)

        dfs(root, val)
        return ans