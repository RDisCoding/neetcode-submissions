class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        s = "".join(i for i in s if i.isalnum())
        
        i = 0
        j = len(s)-1
        
        while i<=j:
            if s[i] != s[j]: return False
            else:
                i+=1; j-=1
        return True