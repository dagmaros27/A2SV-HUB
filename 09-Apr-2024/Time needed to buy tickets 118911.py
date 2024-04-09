# Problem: Time needed to buy tickets - https://leetcode.com/problems/time-needed-to-buy-tickets/

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        i = 0
        while tickets[k] >0 :
            if i == len(tickets):
                i = 0
            if tickets[i] > 0:
                tickets[i] -= 1
                ans += 1
            i += 1
        return ans
# for queue implementation we can add the (value, index) in the queue and add and pop till that index is 0

