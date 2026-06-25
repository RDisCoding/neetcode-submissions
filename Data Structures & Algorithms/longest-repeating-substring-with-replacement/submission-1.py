class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        m = defaultdict(int)
        maxf = 0
        j = 0
        mx = 0
        for i in range(len(s)):
            m[s[i]] +=1
            maxf = max(maxf, m[s[i]])
            while i-j+1 - maxf > k:
                m[s[j]]-=1
                j+=1
            mx = max(mx, i-j+1)
        
        return mx