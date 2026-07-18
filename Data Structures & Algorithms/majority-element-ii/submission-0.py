class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        res = []
        for n,v in c.items():
            if v > (len(nums)//3):
                res.append(n)
        
        return res