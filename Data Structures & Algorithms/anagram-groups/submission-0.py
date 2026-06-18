class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            mapping[key].append(s)
        return list(mapping.values())