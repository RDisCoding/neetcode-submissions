class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        h = defaultdict(list)

        for s in strs:
            x = "".join(sorted(s))
            h[x].append(s)
        
        return list(h.values())