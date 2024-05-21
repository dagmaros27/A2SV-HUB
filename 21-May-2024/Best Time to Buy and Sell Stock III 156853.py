# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf')] * 5 for _ in range(len(prices))]

        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][1] = max(-prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1] + prices[i], dp[i-1][2])

            if i >= 2:
                dp[i][3] = max(dp[i-1][2] - prices[i], dp[i-1][3])

            if i >= 3:
                dp[i][4] = max(dp[i-1][3] + prices[i], dp[i-1][4])
        
        return max(dp[len(prices)-1] + [0])
        