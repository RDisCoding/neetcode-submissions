class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(i, res):
            if i == len(nums): 
                ans.append(res.copy())
                return
            res.append(nums[i])
            bt(i+1, res)
            res.pop()
            bt(i+1, res)
        bt(0, [])
        return ans
        
