class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0
        templist = []
        for i,ns in enumerate(nums):
            for index,n in enumerate(nums):
                if ns + n == target:
                    print(ns)
                    print(n)
                    print(i)
                    templist.append(i)
                    templist.append(index+1)
                    break
                break
        return templist

            