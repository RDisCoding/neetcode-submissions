class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0]>0: return []
        res = []
        n = len(nums)
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            j=i+1; k = n - 1
            while j<k:
                total = nums[i] + nums[j] + nums[k]
                print(total)
                if total > 0: 
                    k-=1
                elif total<0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return res


        