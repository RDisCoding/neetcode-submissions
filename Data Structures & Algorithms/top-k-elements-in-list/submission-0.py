class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        csort = sorted(c.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for x in range(k):
            ans.append(csort[x][0])
        return ans