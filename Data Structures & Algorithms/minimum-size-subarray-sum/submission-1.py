class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0
        ans = float('inf')
        
        for right in range(len(nums)):
            curr += nums[right]
            while curr >= target:
                curr-=nums[left]
                ans = min(ans, right-left+1)
                left +=1
        if ans == float('inf'):
            return 0
        return ans

        