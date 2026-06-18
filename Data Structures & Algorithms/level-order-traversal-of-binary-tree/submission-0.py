# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        q.append(None)
        ans = []
        vals = []
        while q:
            curr = q.popleft()
            if not curr: 
                ans.append(vals)
                vals = []
                if q: 
                    q.append(None)
                else:
                    break
            else:
                vals.append(curr.val)
                if curr.left: 
                    q.append(curr.left)
                if curr.right: 
                    q.append(curr.right)
        return ans