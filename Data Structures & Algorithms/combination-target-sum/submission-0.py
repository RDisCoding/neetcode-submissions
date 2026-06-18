class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, combo, total):
            if total==target:
                res.append(combo.copy())
                return
            if total>target or i>=len(nums):
                return
            
            combo.append(nums[i])
            bt(i, combo, total+nums[i])

            combo.pop()
            bt(i+1, combo, total)

        bt(0, [], 0)
        return res