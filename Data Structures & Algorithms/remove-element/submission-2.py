class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0

        i = 0
        while i < len(nums):
            while nums and nums[-1] == val:
                nums.pop()
            if not nums: return 0
            
            if nums[i] == val:
                nums[i] = nums[-1]
                nums.pop()
            i+=1

        return len(nums)
        
