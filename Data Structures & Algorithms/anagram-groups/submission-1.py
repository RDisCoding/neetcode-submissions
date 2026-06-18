class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sset = defaultdict(list)
        for i in strs:
            c = "".join(sorted(i))
            sset[c].append(i)
        
        return list(sset.values())