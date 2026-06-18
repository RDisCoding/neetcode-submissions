class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for j in range(len(s)):
            count[s[j]] = 1 + count.get(s[j], 0)

            while j-l+1 - max(count.values()) >k:
                count[s[l]] -=1
                l+=1
                
            res = max(res, j - l + 1)
        return res