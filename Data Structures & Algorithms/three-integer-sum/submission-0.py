class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i,n in enumerate(nums):
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+ nums[right] + n == 0:
                    ans.add((nums[left],nums[right],n))
                    left+=1
                    right-=1
                elif nums[left] + nums[right] + n > 0:
                    right-=1
                else:
                    left+=1
        return list(ans)