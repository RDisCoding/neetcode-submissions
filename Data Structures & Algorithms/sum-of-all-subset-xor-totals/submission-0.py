class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        subset = []
        def bt(i):
            if i>=len(nums):
                if not subset: 
                    return
                ans = subset[0]
                for i in range(1, len(subset)):
                    ans ^= subset[i]
                res.append(ans)
                return
            
            subset.append(nums[i])
            bt(i+1)

            subset.pop()
            bt(i+1)
        
        bt(0)
        return sum(res)
        