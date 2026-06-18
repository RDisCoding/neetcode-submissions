class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0
        for c in s:
            if c == '(':
                res.append(c)
                cnt+=1
            elif c == ')':
                if cnt>0:
                    res.append(c)
                    cnt -=1
            else:
                res.append(c)
        
        filtered = []
        for c in res[::-1]:
            if c == '(' and cnt>0:
                cnt -=1
            else:
                filtered.append(c)
        return "".join(filtered[::-1])