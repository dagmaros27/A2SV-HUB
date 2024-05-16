# Problem: Integer Break - https://leetcode.com/problems/integer-break/


class Solution:
    def integerBreak(self, n: int) -> int:
        # @cache
        # def dp(prod):
        #     if prod == n:
        #         return prod
            
        #     mxm = 0
        #     for i in range(1, prod):
        #         mxm = max(mxm, i * dp(prod - i))
            
        #     return mxm
        
        # return dp(n)

        if n==0:
            return 0
        if n <= 2:
            return 1
        if n == 3:
            return 2
        dp = [0] * (n + 1)
        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            dp[i] = max(2 * dp[i - 2], 3 * dp[i - 3])
        return dp[n]