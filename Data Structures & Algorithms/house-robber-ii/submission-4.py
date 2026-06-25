class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            N = len(nums)
            nums.append(0)
            print(nums)
            for i in range(N-3, -1, -1):
                nums[i] += max(nums[i+2], nums[i+3])
            
            return max(nums[0], nums[1]) if len(nums) > 2 else nums[0]
        
        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))