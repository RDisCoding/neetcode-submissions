class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def bt(i, res):
            if i == len(nums): 
                ans.append(res.copy())
                return
            res.append(nums[i])
            bt(i+1, res)
            res.pop()
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            bt(i+1, res)
        bt(0, [])
        return ans
        