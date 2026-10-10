class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for n in nums:
                if i + n == target:
                    second = i
                    first = n

        index1 = nums.index(first)
        nums[index1] = " "
        index2 = nums.index(second)

        listtemp = []
        listtemp.append(index1)
        listtemp.append(index2)
        return listtemp
