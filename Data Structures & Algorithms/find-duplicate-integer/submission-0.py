class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sset = set()
        for n in nums:
            if n in sset:
                return n
            else:
                sset.add(n)
                