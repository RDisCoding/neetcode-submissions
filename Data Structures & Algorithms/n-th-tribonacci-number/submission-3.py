class Solution:
    def tribonacci(self, n: int) -> int:
        if n ==0: return 0
        if n == 1: return 1
        if n==2: return 1

        p1 = 0
        p2 = 1
        p3 = 1
        for i in range(3, n+1):
            temp1, temp2 = p3, p2
            p3 += p1 + p2
            p2, p1 = temp1, temp2

        return p3