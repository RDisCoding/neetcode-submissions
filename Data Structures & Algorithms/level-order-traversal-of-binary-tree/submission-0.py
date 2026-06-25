# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []
        temp = []

        q = deque()
        q.append(root)
        q.append(None)

        while q:
            popped = q.popleft()
            if popped:
                temp.append(popped.val)
                if popped.left: q.append(popped.left)
                if popped.right: q.append(popped.right)
            else:
                res.append(temp)
                if not q: 
                    break
                q.append(None)
                temp = []
            
        return res
