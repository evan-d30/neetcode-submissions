class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            d[n] = d.get(n,0)+1
            if d[n] >= len(nums) /2:
                return n
