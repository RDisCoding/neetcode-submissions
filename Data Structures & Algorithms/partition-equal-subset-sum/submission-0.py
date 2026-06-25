class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = 0
        for n in nums:
            target += n

        def bt(i, total, target):
            if i == len(nums) or total > target - total: 
                return False
            if total == target - total:
                return True
            print((i, total))
            a1 = bt(i+1, total + nums[i], target)
            a2 = bt(i+1, total, target)
            return a1 or a2
        return bt(0,0,target)
        