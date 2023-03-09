class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for string in strs:
            s = ''.join(sorted(string))
            res[s].append(string)
        return res.values()