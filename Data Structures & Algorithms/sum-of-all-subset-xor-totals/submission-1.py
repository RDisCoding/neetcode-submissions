class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def bt(i, total):
            if i==len(nums):
                return total

            return bt(i+1, total^nums[i]) + bt(i+1, total)
        
        return bt(0,0)
        