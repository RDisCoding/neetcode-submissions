class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n>>i)&1 # 1st binary operation using and
            res = res | (bit << (31 - i)) # 2nd binary operation using or
        
        return res