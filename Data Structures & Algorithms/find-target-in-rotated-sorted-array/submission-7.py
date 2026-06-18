class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        l=0
        r = len(nums) - 1

        while l< r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        d = l
        print(d)

        n = len(nums)
        if d == 0:
            return self.binSearch(0, n-1, nums, target)
        if target>=nums[0]:
            return self.binSearch(0, d-1, nums, target)
        else:
            return self.binSearch(d, n-1, nums, target)
    
    def binSearch(self, left, right, nums, target):
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right = mid - 1
            else:
                left = mid+1
        return -1