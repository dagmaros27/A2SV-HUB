# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if (x == y):
                continue
            else:
                y = - (abs(y) - abs(x))
                heappush(stones,y)
        if len(stones):
            return abs(stones[0])
        else:
            return 0
            

        return 0

        