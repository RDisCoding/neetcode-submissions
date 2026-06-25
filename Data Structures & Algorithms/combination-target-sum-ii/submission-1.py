class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(i, total, ans):
            if total== target:
                res.append(ans.copy())
                return
                
            if i == len(candidates) or total > target:
                return
            
            
            total += candidates[i]
            ans.append(candidates[i])
            bt(i+1, total, ans)

            total -= candidates[i]
            ans.pop()
            bt(i+1, total, ans)

        bt(0, 0, [])
        
        seen = set()
        unique = []
        for i in res:
            t = tuple(sorted(i))
            if t not in seen:
                seen.add(t)
                unique.append(i)
        return unique

