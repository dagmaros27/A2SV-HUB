# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #brute force
        #this approach's time complexity - O(k*n) 
        # while k:
        #     idx = piles.index(max(piles))

        #     piles[idx] -= piles[idx]//2
        #     k -= 1  
        # return sum(piles)

        piles = [-i for i in piles]
        heapify(piles)
        while k:
            mxm = heappop(piles)
            mxm = mxm//2
            heappush(piles,mxm)
            k -=1
        piles = [-i for i in piles]

        return sum(piles)


        

        

        