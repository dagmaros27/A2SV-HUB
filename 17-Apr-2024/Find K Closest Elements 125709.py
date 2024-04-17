# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = [abs(i-x) for i in arr]
        print(diff)
        heap = [pair for pair in zip(diff,arr)]

        heapify(heap)
        ans = []
        
        for _ in range(k):
            ans.append(heappop(heap)[1])
        
        ans.sort()

        return ans
        