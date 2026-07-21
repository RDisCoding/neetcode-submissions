class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        res = 0
        sign = 0 if x>0 else 1
        x = abs(x)
        while x:
            rem = x%10

            if res > MAX/10 or res < MIN/10: return 0
            if res == MAX/10 and rem > MAX%10: return 0

            res = res*10 + rem
            x//=10
        
        if sign :
            res *= -1
        return res