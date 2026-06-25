class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        cm = max(nums[:k])
        stack = [cm]
        j = 0 
        for i in range(k, len(nums)):
            print(f"{i}: {nums[i]}")
            print(f"{j}: {nums[j]}")
            print(stack)
            ans.append(stack[-1])
            x = nums[j]
            if x == stack[-1]:
                stack.pop()
            j+=1
            y = nums[i]
            if stack:
                if y>=stack[-1]:
                    stack.pop()
                    stack.append(y)
            else:
                stack.append(max(nums[j:i+1]))     

        ans.append(stack[-1])       
        return ans