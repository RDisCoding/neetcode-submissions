class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        ans = sorted(d, key = lambda x: d[x], reverse=True)
        return ans[:k]
        