class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        templist = []
        for n in nums:
            if n < 0:
                continue
            elif n + 1 not in nums:
                templist.append(n+1)
        if 1 not in nums:
            templist.append(1)
            
        return min(templist)


