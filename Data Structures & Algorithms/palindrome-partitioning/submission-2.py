class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []

        def ispal(s):
            if not s or len(s) == 1: 
                return True
            if s[0] == s[-1] and ispal(s[1:-1]):
                return True
            return False

        def bt(i):
            if i==len(s):
                res.append(temp.copy())
                return 
            for j in range(i, len(s)):
                if ispal(s[i:j+1]):
                    temp.append(s[i:j+1])
                    bt(j+1)
                    temp.pop()
        
        bt(0)
        return res
