class Solution:
    def sortColors(self, nums: List[int]) -> None:
        templist = []
        permlist = nums[:]
        while len(nums) != len(templist):
            count = None
            for n in permlist:
                if count is None:
                    count = n
                elif count > n:
                    count = n
            templist.append(count)
            permlist.remove(count)
        nums[:] = templist

