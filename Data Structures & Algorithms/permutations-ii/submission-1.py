class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = set()
        def bt(idx, perms):
            state = (idx, tuple(perms)) #
            if state in visit:
                return
            visit.add(state)
            if idx == len(nums):
                res.append(perms.copy())
                return

            for i in range(len(perms)+1):
                perms.insert(i, nums[idx])
                bt(idx+1, perms)
                perms.pop(i)
        
        bt(0, [])
        print(res)
        return list(map(list, set(map(tuple, res))))