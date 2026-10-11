class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        d = dict()
        for n in nums:
            d[n] = d.get(n,0)+1

        numlist = list(d.keys())
        secondtemplist = numlist[:]
        templist = []
        while len(templist) != len(numlist):
            count = None
            for n in secondtemplist:
                if count is None:
                    count = n
                elif n < count:
                    count = n
            templist.append(count)
            secondtemplist.remove(count)   
        finallist = []
        for n in templist:
            for _ in range(d[n]):
                finallist.append(n)
        return finallist
            