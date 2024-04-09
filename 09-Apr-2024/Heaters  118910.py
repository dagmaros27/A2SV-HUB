# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #minmax
        heaters.sort()

        def bs(house):
            l, h = 0,len(heaters)-1
            rad = float('inf')
            while l < h:
                m = (l+h)//2
                if heaters[m] == house:
                    rad = 0
                    break
                elif heaters[m] < house:
                    rad = min(rad, abs(heaters[m]- house))
                    l  = m+1
                else:
                    rad = min(rad, abs(heaters[m]- house))
                    h  = m
            rad = min(rad, abs(heaters[l] - house))
            return rad
        ans = 0

        for h in houses:
            cur = bs(h)
            ans = max(ans,cur)
        
        return ans
            


