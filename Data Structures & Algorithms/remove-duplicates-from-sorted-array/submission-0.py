class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in nums:
            if nums[k] == i:
                continue
            k+=1
            nums[k] = i
        return k+1