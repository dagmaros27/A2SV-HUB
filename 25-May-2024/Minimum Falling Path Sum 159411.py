# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        dp[0] = matrix[0]

        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min([dp[i-1][j],dp[i-1][j+1], dp[i-1][j-1]])
            
        return min(dp[n-1])



        