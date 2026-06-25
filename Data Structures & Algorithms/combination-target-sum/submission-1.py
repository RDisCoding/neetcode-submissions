class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, cur, target):
            if i >= len(nums) or target < 0:
                return 

            if target == 0:
                print(cur)
                res.append(cur.copy())
                return

            cur.append(nums[i])
            bt(i, cur, target-nums[i])
            cur.pop()
            bt(i+1, cur, target)

        bt(0, [], target)
        return res