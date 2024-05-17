# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i,state):
            if i >= len(prices):
                return 0
            if state == "buy":
                return max(dp(i+1, "sell") - prices[i] , dp(i+1, "buy")) 
            else:
                return max(dp(i+1, "sell"), dp(i+2, "buy") + prices[i])
        return dp(0, "buy")    
        