class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(i, j):
            while i<=j:
                mid = i + (j-i)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            return -1
        
        i = 0
        j = len(nums)-1
        
        while i<j:
            mid = i + (j-i)//2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid
        
        print(j)
        pt = j

        if pt == 0: return bs(0,len(nums)-1)
        elif nums[0] <= target: return bs(0, pt-1)
        else: return bs(pt, len(nums)-1)
