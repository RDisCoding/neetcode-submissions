class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in mapper:
                mapper[nums[i]] = i
            else:
                return [mapper[target-nums[i]], i]
             
        