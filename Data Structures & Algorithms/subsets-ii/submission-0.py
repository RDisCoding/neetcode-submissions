class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        def bt(i):
            if i>=len(nums):
                
                res.add(tuple(sorted(subset.copy())))
                return 

            subset.append(nums[i])
            bt(i+1)

            subset.pop()
            bt(i+1)
        
        bt(0)
        res = [list(t) for t in sorted(res)]
        return res
