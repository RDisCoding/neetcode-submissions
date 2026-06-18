# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        def isSame(p, q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        q = deque([root])
        while q:
            popped = q.popleft()
            if popped.left: 
                q.append(popped.left)
            if popped.right: 
                q.append(popped.right)

            if popped.val == subRoot.val:
                self.ans = isSame(popped, subRoot)
                if self.ans == True: break
        return self.ans