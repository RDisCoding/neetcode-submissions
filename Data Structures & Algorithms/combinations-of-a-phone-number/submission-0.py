class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []

        m = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j','k','l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        res = []

        def bt(i, s):
            if i==len(digits): 
                res.append(s)
                return
            
            for ch in m[int(digits[i])]:
                s+=ch
                bt(i+1, s)
                s = s[:-1]
        
        bt(0, "")

        return res
            
