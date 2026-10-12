class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            sort = sorted(i)
            key = "".join(sort)
            if key not in group:
                group[key] = []
            group[key].append(i)                   
        return list(group.values())