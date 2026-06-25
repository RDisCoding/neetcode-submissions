class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def bt(i, ans, k):
            if i>n+1: 
                return
            if len(ans) == k:
                res.append(ans.copy())
                return
            ans.append(i)
            bt(i+1, ans, k)
            ans.pop()
            bt(i+1, ans, k)
        bt(1, [], k)
        return res