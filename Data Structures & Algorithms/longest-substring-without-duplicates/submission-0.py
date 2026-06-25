class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        j = 0 
        sset = set()
        for i in range(len(s)):
            while s[i] in sset:
                sset.remove(s[j])
                j+=1
            sset.add(s[i])
            longest = max(longest, i-j+1)
        return longest