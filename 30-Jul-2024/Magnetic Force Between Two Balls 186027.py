# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        ans = 0
        position.sort() 

        def func(minDist):
            prev = position[0]
            count = 1

            for i in range(1,len(position)):
                if position[i]-prev>=minDist:
                    prev = position[i]
                    count+=1
                if count==m:
                    return True
            return False

        l,h = 1,(position[-1]-position[0])
        while l<=h:
            mid = (l+h)//2
            if func(mid):
                ans = mid
                l=mid+1
            else:
                h=mid-1

        return ans

        