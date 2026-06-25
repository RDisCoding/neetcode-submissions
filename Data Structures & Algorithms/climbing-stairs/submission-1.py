class Solution:
    def climbStairs(self, n: int) -> int:
        one,two =1,1

        for i in range(n-1):
            print(one)
            print(two)
            print()
            temp = one
            one += two
            two = temp
        
        return one