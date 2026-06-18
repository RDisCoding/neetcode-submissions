class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        cnt = 0
        j = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in sset:
                sset.remove(s[j])
                j+=1
            sset.add(s[i])
            ans = max(ans, i-j+1)
        return ans