# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heapify(matrix)
        k -= 1
        while k:
            if matrix:
                x =heappop(matrix)
                heappop(x)
                if x:
                    heappush(matrix,x)
            k -= 1 

        
        return heappop(heappop(matrix))
            


        