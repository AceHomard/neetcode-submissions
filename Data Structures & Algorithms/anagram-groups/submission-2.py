class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[frozenset(Counter(s).items())].append(s)
        return list(res.values())