class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = minP = ans = nums[0]

        for i in nums[1:]:
            candidates = [i, maxP*i, minP*i]
            maxP = max(candidates)
            minP = min(candidates)
            ans = max(ans, maxP)
        
        return ans