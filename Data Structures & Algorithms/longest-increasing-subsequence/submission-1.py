class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mx = 0
        def bt(i, curr):
            nonlocal mx
            mx = max(mx, len(curr))
            if i == len(nums):
                return
            if not curr or nums[i] > curr[-1]:
                curr.append(nums[i])
                print(curr)
                bt(i+1, curr)
                curr.pop()
                print(curr)
            bt(i+1, curr)
            
        bt(0, [])
        return mx
