class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for i in range(len(nums) - k + 1):
            mx = nums[i]
            for j in range(i, i+k):
                mx = max(mx, nums[j])
            output.append(mx)
    
        return output