# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = max(prices)
        ans = 0

        for r in range(len(prices)):
            buy = min(buy, prices[r])
            ans = max(ans, prices[r]-buy)
        return ans