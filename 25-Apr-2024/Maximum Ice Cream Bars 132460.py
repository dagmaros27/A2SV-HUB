# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        maxNum = max(costs)
        counter = [0]* (maxNum+1)

        for cost in costs:
            counter[cost] += 1
        ans = 0
        total= 0
        for i in range(maxNum+1):
            while counter[i] > 0:
                total += i 
                if total <= coins:
                    ans += 1
                counter[i] -= 1
                
        return ans