# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:


        @cache
        def dp(l, r):
            if r-l + 1 == 3:
                return values[l] * values[l+1] * values[l+2]
            if r-l + 1 < 3:
                return 0
            ans = float("inf")
            for i in range(l+1, r):
                ans = min(ans, values[l]*values[i]*values[r] + dp(l, i) + dp(i, r))
            return ans
        return dp(0, len(values)-1)