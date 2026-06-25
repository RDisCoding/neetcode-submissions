class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, total, ans):
            if i ==len(nums) or total > target: 
                return
            if total == target:
                res.append(ans.copy())
                return
            total += nums[i]
            ans.append(nums[i])
            bt(i, total, ans)
            total -= nums[i]
            ans.pop()
            bt(i+1, total, ans)
        bt(0, 0, [])
        return res
