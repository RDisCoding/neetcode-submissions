class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hset = set(nums)
        print(hset)
        for n in nums:
            if n-1 in hset: continue
            else:
                ans = 0
                while n in hset:
                    ans +=1
                    n+=1
                res = max(res, ans)

        return res