class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def bt(i):
            if i>=len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            bt(i+1)

            x = subset.pop()
            while i<len(nums) and nums[i] == x:
                i+=1
            bt(i)
        
        bt(0)
        return res
