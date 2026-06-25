class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]

        def check(s1, s2):
            n1 = len(s1)
            n2 = len(s2)
            if n1 > n2:
                s1 = s1[:n2]
            elif n2 > n1:
                s2 = s2[:n1]
            idx = len(s1)
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    idx = i
                    break
            return idx

        for i in range(1, len(strs)):
            idx = check(pre, strs[i])
            pre = pre[:idx]
        
        return pre