from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count = defaultdict(int)
        for i, x in enumerate(nums):
            if count[x] > 0:
                return True
            count[x] += 1
            if i >= k:
                count[nums[i - k]] -= 1
        return False

                
                
                