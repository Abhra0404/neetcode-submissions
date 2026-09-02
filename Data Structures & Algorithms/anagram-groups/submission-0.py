class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        groups = {}
        for s in strs:
            key = sorted(s)
            key = "".join(key)
            groups.setdefault(key, []).append(s)
        for i in groups:
            ans.append(groups[i])
        return ans