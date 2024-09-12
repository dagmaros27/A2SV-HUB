# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxm = 0

        l,r = 0,len(height)-1

        while l < r:
            curr = min(height[r],height[l]) * (r-l)
            mxm = max(mxm,curr)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            
        return mxm
        