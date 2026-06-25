class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count = defaultdict(int)
        for x in t:
            count[x] +=1
        have, need = 0, len(count)
        window = defaultdict(int)

        res, reslen = "",float('inf')

        j = 0
        for i in range(len(s)):
            window[s[i]]+=1
            if s[i] in count and window[s[i]]==count[s[i]]:
                have +=1

                while have == need:
                    print(f"have: {have}")
                    print(i)
                    print(j)
                    window[s[j]]-=1
                    if s[j] in count and window[s[j]]<count[s[j]]:
                        have -=1
                    if reslen > i-j+1:
                        reslen = i-j+1
                        res = s[j:i+1]
                    j+=1
                 

        return res