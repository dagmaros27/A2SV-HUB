# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        i = 1
        while i*i <= n:
            arr.append(i*i)
            i += 1
        if arr[-1] == n:
            return 1

        @cache
        def dp(amount):
            if amount < 0 :
                return inf
            if amount == 0:
                return 0
            
            mnm = inf

            for perfect in arr :
                mnm = min(mnm, 1+ dp(amount-perfect))
            
            return mnm

        res = dp(n)

        return res if res != inf else 0
        
        