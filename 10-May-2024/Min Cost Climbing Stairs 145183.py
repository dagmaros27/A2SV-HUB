# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1]*1000
        def dp(i):
            if i == 0 or i == 1:
                return cost[i]
            if i == len(cost):
                return min(dp(i-1),dp(i-2))
            if memo[i] != -1:
                return memo[i]
            res = min(dp(i-1)+ cost[i],dp(i-2) + cost[i])
            memo[i] = res
            return res


        return dp(len(cost))