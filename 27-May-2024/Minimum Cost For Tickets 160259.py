# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        
        memo = {}
        
        def dp(day):
            if day in memo:
                return memo[day]
            
            if day > 365:
                return 0
            
            if day not in travel_days:
                memo[day] = dp(day + 1)
                return memo[day]
            
            one_day = costs[0] + dp(day + 1)
            seven_day = costs[1] + dp(day + 7)
            thirty_day = costs[2] + dp(day + 30)
            
            memo[day] = min(one_day, seven_day, thirty_day)
            return memo[day]
        
        return dp(1)