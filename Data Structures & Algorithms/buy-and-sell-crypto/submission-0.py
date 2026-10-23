class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = ans = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                ans = max(ans, prices[right] - prices[left])
        return ans
                    

