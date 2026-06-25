class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def count(n):
            cnt = 0
            while n:
                cnt+=1
                n &= (n-1)
            res.append(cnt)

        for i in range(n+1):
            count(i)
        
        return res