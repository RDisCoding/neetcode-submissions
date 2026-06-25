class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # go through the list
        # make a directed graph like z -> o
        # apply post order dfs
        # backtrack from there to the starting point and append each node in a list along the way
        # finally join the list and reverse it
        # that's all


        adj = { c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visit = {} # false = visited but not in current path; true = in current path

        res = []

        def dfs(c):
            if c in visit: return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei): # detected cycle
                    return True

            visit[c] = False
            res.append(c)
        
        for c in adj: 
            if dfs(c): return ""
        return "".join(res[::-1])
        

