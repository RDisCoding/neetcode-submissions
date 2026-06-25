class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j = 0
        visited = set()
        ans = 0
        for i in range(len(s)):
            if s[i] not in visited:
                visited.add(s[i])
            else:
                while s[i] in visited:
                    visited.remove(s[j])
                    j+=1
            visited.add(s[i])
            ans = max(ans, i-j+1)
            print(ans)
        return ans