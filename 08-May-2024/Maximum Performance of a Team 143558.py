# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        effed = sorted([[efficiency[i], speed[i]] for i in range(len(speed))],reverse=True)

        heap = []
        total_speed = 0
        ans = 0
        for e,s in effed:
            
            heappush(heap,s)

            total_speed += s

            if len(heap) > k:
                total_speed -= heappop(heap)
            
            ans = max(ans,(total_speed * e))


        return ans%(10**9+7)





        