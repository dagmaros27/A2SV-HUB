# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dp(idx,total):
            if idx >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            if (idx,total) in memo:
                return memo[(idx,total)]
            
            res =  sum([dp(idx, total+ coins[idx]), dp(idx+1, total)]) 
            memo[(idx,total)] = res

            return res


      
        return dp(0,0)