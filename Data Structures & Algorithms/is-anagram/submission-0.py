class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = dict()
        dt = dict()
        for l in s:
            ds[l] = ds.get(l,0) +1
        for l in t:
            dt[l] = dt.get(l,0) +1

        return dt == ds