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
        ans = []
        res = []
        q.append(None)
        while q:
            popped = q.popleft()
            if not popped:
                res.append(ans)
                ans = []
                if not q: return res
                else: 
                    q.append(None)
                    continue
            ans.append(popped.val)
            if popped.left: q.append(popped.left)
            if popped.right: q.append(popped.right)
            
        return res