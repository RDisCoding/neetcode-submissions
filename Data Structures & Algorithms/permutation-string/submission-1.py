class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        l = 0
        for i in range(len(s1), len(s2)+1):
            current = Counter(s2[l:i])
            print(current)
            if current == target:
                return True
            else:
                l+=1
        return False