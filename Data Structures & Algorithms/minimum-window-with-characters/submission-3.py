class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for i in t:
            countT[i] = 1 + countT.get(i, 0)
        
        have,need = 0,len(countT)
        res, resLen = [-1,-1], float('inf')

        j = 0
        for i in range(len(s)):
            c = s[i]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have +=1
            
            while have == need:
                if i-j+1 < resLen:
                    res = [j,i]
                    resLen = i-j+1

                window[s[j]] -= 1
                if s[j] in countT and window[s[j]] < countT[s[j]]:
                    have -=1
                j+=1
        j,i = res
        return s[j:i+1] if resLen != float('inf') else ""