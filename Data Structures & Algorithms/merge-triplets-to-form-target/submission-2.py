class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = [0,0,0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                valid[0] = max(valid[0], t[0])
                valid[1] = max(valid[1], t[1])
                valid[2] = max(valid[2], t[2])

        return valid == target