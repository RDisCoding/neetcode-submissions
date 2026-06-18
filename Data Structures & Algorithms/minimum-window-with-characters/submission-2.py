class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        l = 0
        minl = float('inf')
        ans = ""
        print(target)
        for i in range(len(t), len(s)+1):
            current = Counter(s[l:i])
            print(current)
            while target <= current:
                print(i)
                if i-l+1 < minl:
                    minl = i-l+1
                    ans = s[l:i]
                current[s[l]]-=1
                l+=1
        return ans