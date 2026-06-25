class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(len(nums)):
            c =0
            i = 0
            while i+1<len(nums):
                if nums[i] <= nums[i+1]: 
                    c+=1
                else:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                i+=1
            if c == len(nums)-1: break