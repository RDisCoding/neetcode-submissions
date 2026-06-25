class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bt(i, total, ans):
            if total == target:
                res.append(ans.copy())
                return
                
            if i == len(candidates) or total > target:
                return

            
            
            total += candidates[i]
            ans.append(candidates[i])
            bt(i+1, total, ans)

            total -= candidates[i]
            ans.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            bt(i+1, total, ans)

        bt(0, 0, [])
        
        return res

