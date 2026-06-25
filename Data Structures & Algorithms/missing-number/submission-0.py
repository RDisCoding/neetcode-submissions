class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a1 = n
        for i in range(n):
            a1^=i
        for i in nums:
            a1^=i
        
        return a1