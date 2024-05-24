# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        n = 1
        for i in range(len(triangle)):
            dp.append([0]*n)
            n += 1

        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == i:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])

        return min(dp[-1])



        