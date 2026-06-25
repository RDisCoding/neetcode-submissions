class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1: return 0 if nums[0]==target else -1
        
        def binarysearch(i, j, target):
            while i<=j:
                mid = i + (j-i)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
            return -1
        
        i = 0
        j = len(nums)-1
        while i<j:
            mid = i + (j-i)//2
            if nums[mid]>nums[j]:
                i = mid+1
            else:
                j = mid
        
        pt = j
        if target == nums[pt]: 
            return pt
        elif pt == 0:
            return binarysearch(0, len(nums)-1, target)
        elif nums[0]<=target<=nums[pt-1]:
            return binarysearch(0, pt-1, target)
        else:
            return binarysearch(pt, len(nums)-1, target)
        