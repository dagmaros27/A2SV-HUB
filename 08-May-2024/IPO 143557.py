# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        capHeap = [[capital[i],profits[i]] for i in range(len(profits))]
        
        heapify(capHeap)
        
        proHeap = []
        
        while k:
            while capHeap and capHeap[0][0] <= w:
                c,p = heappop(capHeap)
                heappush(proHeap, -p)
            
            if proHeap:             
                p = heappop(proHeap)
                w += abs(p)
                k -= 1
            else:
                break
            

        return w



        