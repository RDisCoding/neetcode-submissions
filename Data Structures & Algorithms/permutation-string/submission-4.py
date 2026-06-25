class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        cs1 = [0]*26
        cs2 = [0]*26

        for i in range(len(s1)):
            cs1[ord(s1[i])-ord('a')]+=1
            cs2[ord(s2[i])-ord('a')]+=1

        print(cs1)
        print(cs2)

        matches = 0
        for i in range(26):
            if cs1[i]==cs2[i]: matches+=1

        print(matches)
        
        j = 0
        for i in range(len(s1), len(s2)):
            print(i)
            if matches == 26: return True
            idx1 = ord(s2[i])-ord('a')
            cs2[idx1]+=1
            if cs2[idx1] == cs1[idx1]: matches+=1
            elif cs2[idx1]-1==cs1[idx1]: matches -=1

            print(cs1)
            print(cs2)
            print(matches)

            idx2 = ord(s2[j])-ord('a')
            cs2[idx2]-=1
            j+=1
            if cs2[idx2] == cs1[idx2]: matches+=1
            elif cs2[idx2]+1==cs1[idx2]: matches -=1 

            print(cs1)
            print(cs2)
            print(matches)
            
        return matches==26