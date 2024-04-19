# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

from typing import List
from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        heap = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            arr.append(diff)

        counter = 0
        for diff in arr:
            
            if diff <= 0:
                counter += 1
                continue
            
            heappush(heap,diff)

            if len(heap) > ladders:
                mnm = heappop(heap)
                if mnm > bricks:
                    return counter
                bricks -= mnm
            counter += 1
            

        return counter