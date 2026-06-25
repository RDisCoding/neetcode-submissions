class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for _ in range(len(nums)):
            cnt = 0
            i = 0
            while i+1<len(nums):
                if nums[i] <= nums[i+1]:
                    cnt+=1
                else:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                i+=1
            if cnt == len(nums)-1: break
        return nums