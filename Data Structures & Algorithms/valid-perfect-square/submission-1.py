class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        low = 1
        high = num//2

        while low < high:
            mid = low + (high-low)//2
            print(mid)
            if mid**2 == num:
                return True
            elif mid**2 > num:
                high = mid 
            else:
                low = mid + 1
        
        return False