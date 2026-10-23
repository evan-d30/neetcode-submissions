from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        ans = curr = left = 0
        for right in range(len(s)):
            count[s[right]]+=1
            maxf = max(list(count.values()))
            while (right - left + 1) - maxf > k:
                count[s[left]]-=1
                left+=1
            ans = max(ans, right-left+1)
        return ans


        