class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        cs1 = [0]*26
        cs2 = [0]*26

        matches = 0
        for i in range(len(s1)):
            cs1[ord(s1[i])-ord('a')] +=1
            cs2[ord(s2[i])-ord('a')] +=1

        for i in range(26):
            matches += 1 if cs1[i]==cs2[i] else 0

        j = 0
        for i in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[i]) - ord('a')
            cs2[index] += 1
            if cs1[index] == cs2[index]:
                matches +=1
            elif cs1[index] + 1 == cs2[index]:
                matches -=1
            
            index = ord(s2[j]) - ord('a')
            cs2[index] -=1
            if cs1[index] == cs2[index]:
                matches+=1
            elif cs1[index]-1 == cs2[index]:
                matches-=1
            j+=1

        return matches==26

