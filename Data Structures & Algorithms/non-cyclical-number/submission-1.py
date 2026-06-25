class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while n:
            total = 0
            while n:
                d = n%10
                total = total + d**2
                n //=10
            n = total
            if n == 1: 
                return True
            if n in visited:
                return False
            visited.add(n)
        
