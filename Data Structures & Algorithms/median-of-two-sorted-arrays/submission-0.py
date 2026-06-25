class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        
        while i<len(nums1): 
            arr.append(nums1[i])
            i+=1
        
        while j<len(nums2):
            arr.append(nums2[j])
            j+=1
        
        s = len(arr)
        if s%2 == 0:
            return (arr[s//2] + arr[s//2 - 1])/2
        else:
            return float(arr[s//2])