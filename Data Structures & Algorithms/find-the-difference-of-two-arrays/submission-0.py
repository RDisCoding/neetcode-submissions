class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        temp = set()
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                temp.add(nums1[i])
        
        ans.append(list(temp))
        temp = set()
        for j in range(len(nums2)):
            if nums2[j] not in nums1:
                temp.add(nums2[j])
        
        ans.append(list(temp))
        return ans