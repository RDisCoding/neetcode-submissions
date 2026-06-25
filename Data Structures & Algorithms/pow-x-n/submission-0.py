class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1
        for i in range(abs(n)):
            a *= x

        return a if n>=0 else 1/a