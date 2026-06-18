class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j= 0
        ans = []
        for i in range(k, len(nums)+1):
            ans.append(max(nums[j:i]))
            j+=1
        return ans