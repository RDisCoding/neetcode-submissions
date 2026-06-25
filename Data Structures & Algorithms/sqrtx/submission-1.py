class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1: return 1
        i = 0
        j = x//2
        while i<=j: 
            mid = i + (j-i)//2
            ans = mid*mid
            if ans == x:
                return mid
            elif ans > x:
                j = mid - 1
            else:
                i = mid + 1
        return j