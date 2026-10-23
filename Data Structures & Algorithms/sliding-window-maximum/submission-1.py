from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        curr = defaultdict(int)
        for i in range(k):
            curr[nums[i]]+=1
        for right in range(k,len(nums)):
            maxnum = max(list(curr.keys()))
            curr[nums[right]]+=1
            curr[nums[right-k]]-=1
            if curr[nums[right-k]]==0:
                del curr[nums[right-k]]
            ans.append(maxnum)
        ans.append(max(list(curr.keys())))
        return ans