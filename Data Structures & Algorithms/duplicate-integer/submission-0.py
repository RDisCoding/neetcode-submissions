class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        for i in nums:
            if i not in visit:
                visit.add(i)
            else:
                return True
        return False