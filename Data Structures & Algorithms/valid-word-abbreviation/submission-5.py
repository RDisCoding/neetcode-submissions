class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1,p2= 0,0

        while p1<len(word) and p2 < len(abbr):
            if abbr[p2].isnumeric() and abbr[p2] != "0":
                k = p2
                while k < len(abbr) and abbr[k].isnumeric():
                    k+=1
                num = int(abbr[p2:k])
                p1 += num
                p2 = k
                print(p1)
                print(p2)
                if p1 > len(word):
                    return False
            else:
                if word[p1] == abbr[p2]:
                    p1 += 1
                    p2 += 1
                else:
                    return False
        
        return p2 == len(abbr)