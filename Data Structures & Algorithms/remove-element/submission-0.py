class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        templist = nums[:]
        for n in templist:
            if n == val:
                nums.remove(n)
        return len(nums)

