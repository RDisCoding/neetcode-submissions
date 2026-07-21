class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            if target - nums[i] in h:
                return sorted([i, h[target-nums[i]]])
            h[nums[i]] = i
