class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        prev = [str2[i:] for i in range(m)]
        prev.append("")

        for i in reversed(range(n)):
            cur = [""]*m
            cur.append(str1[i:])
            for j in reversed(range(m)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j+1]
                else:
                    r1 = str1[i] + prev[j]
                    r2 = str2[j] + cur[j+1] 
                    if len(r1) < len(r2):
                        cur[j] = r1
                    else:
                        cur[j] = r2
            
            prev = cur
                
        return cur[0]