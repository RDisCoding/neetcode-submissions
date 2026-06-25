class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in numset:
                l = 1
                while n+l in numset:
                    l+=1
                longest = max(longest, l)
        return longest