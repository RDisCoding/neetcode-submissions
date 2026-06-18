class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        ans = sorted(freq.items(), key = lambda x: x[1], reverse = True)
        return [n for n,i in ans[:k]]