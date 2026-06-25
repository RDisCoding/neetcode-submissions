class TrieNode:
    def __init__(self, value):
        self.val = value
        self.children = [0]*26
        self.flag = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = TrieNode("#")
        for word in dictionary:
            ptr = root
            for w in word:
                if not ptr.children[ord(w) - ord('a')]:
                    ptr.children[ord(w) - ord('a')] = TrieNode(w)
                ptr = ptr.children[ord(w) - ord('a')]
            ptr.flag = True
        
        n = len(s)
        count = 0
        memo = {}
        def dp(i):
            if i == len(s): return 0
            if i in memo: return memo[i]

            res = 1 + dp(i+1)

            ptr = root
            for j in range(i, len(s)):
                char_idx = ord(s[j]) - ord('a')
                if not ptr.children[char_idx]:
                    break # No more words possible in this path
                
                ptr = ptr.children[char_idx]
                if ptr.flag:
                    # Found a word from s[i:j+1], no extra chars for this segment
                    res = min(res, dp(j + 1))

            memo[i]= res
            return res
        
        return dp(0)