# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)] for i in range(n+1)]
        
        dp[n][0] = dp[n][1] = 0         
        ind = n-1

        while(ind>=0):	
            for buy in range(2):
                if(buy):
                    profit = max(-prices[ind]-fee + dp[ind+1][0], 0 + dp[ind+1][1])				
                else:
                    profit = max(prices[ind] + dp[ind+1][1], 0 + dp[ind+1][0])                 
                dp[ind][buy] = profit				
            ind -= 1    
			
        return dp[0][1]      