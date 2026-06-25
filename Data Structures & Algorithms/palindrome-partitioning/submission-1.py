class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def checkPalindrome(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def bt(start, ans):
            if start == len(s): 
                res.append(ans.copy())
                return
            
            for end in range(start, len(s)):
                if checkPalindrome(start, end):
                    ans.append(s[start:end+1])
                    bt(end+1, ans)
                    ans.pop()

        bt(0,[])

        return res