class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j<len(abbr):
            if abbr[j].isdecimal() and abbr[j] != "0":
                start = j
                while j<len(abbr) and abbr[j].isdecimal():
                    j+=1
                i += int(abbr[start:j])
            elif abbr[j] != word[i]:
                return False
            else:
                i+=1
                j+=1
        print((i,j))
        if i == len(word) and j == len(abbr): 
            return True
        return False