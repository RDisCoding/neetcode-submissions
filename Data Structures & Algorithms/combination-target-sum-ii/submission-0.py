class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # 1 2 2 4 5 6 9
        res = []

        def bt(i, combo, total):
            if total == target:
                print(combo)
                res.append(combo.copy())
                return
            
            if i>=len(candidates) or total > target:
                return

            combo.append(candidates[i])
            print('append')
            print(candidates[i])
            bt(i+1, combo, total + candidates[i])

            x = combo.pop()
            while i+1 < len(candidates) and candidates[i+1] == x:
                i+=1
            print('pop')
            print(x)
            bt(i+1, combo, total)

        bt(0, [], 0)
        return res