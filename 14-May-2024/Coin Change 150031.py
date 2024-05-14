# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(amount):
            if amount < 0 :
                return inf
            if amount == 0:
                return 0
            
            mnm = inf

            for coin in coins:
                mnm = min(mnm, 1+ dp(amount-coin))
            
            return mnm

        res = dp(amount)

        return res if res != inf else -1
