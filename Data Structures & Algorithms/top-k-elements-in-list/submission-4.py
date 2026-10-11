class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for n in nums:
            d[n] = d.get(n,0)+1
        count = 0
        templist = []
        while count != k:
            value = max(d.values())
            key = next(k for k, v in d.items() if v == value)
            templist.append(key)
            count += 1
            d[key] = 0

        return templist
