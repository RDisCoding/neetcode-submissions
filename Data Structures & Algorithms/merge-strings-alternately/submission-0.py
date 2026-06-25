class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1: return word2
        if not word2: return word1

        i,j = 0,0
        newS = ""
        while i<len(word1) and j<len(word2):
            if i<=j:
                newS += word1[i]
                i+=1
            else:
                newS += word2[j]
                j+=1
        
        if i<len(word1):
            newS += word1[i:]
        if j<len(word2):
            newS += word2[j:]
        
        return newS