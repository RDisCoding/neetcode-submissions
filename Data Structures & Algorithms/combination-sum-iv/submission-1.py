class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def bt(total):
            if total in memo:
                return memo[total]
            if total == target: 
                return 1
            if total > target: 
                return 0
            ways = 0
            for i in range(len(nums)):
                ways += bt(total + nums[i])

            memo[total] = ways
            return ways

        return bt(0)
