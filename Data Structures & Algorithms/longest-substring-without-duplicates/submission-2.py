class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        i = 0
        maxl = 0
        visit = set()

        for j in range(len(s)):
            while s[j] in visit:
                visit.remove(s[i])
                i+=1
            visit.add(s[j])
            maxl = max(maxl, j-i+1)
        return maxl