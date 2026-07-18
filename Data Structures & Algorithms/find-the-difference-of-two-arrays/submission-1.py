class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        t = []
        for i in nums1:
            if i not in nums2:
                t.append(i)
        ans.append(t)
        t = []
        for j in nums2:
            if j not in nums1:
                t.append(j)
        ans.append(t)
        return ans

