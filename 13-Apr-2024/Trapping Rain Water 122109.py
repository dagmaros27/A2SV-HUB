# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        stk = []
        
        for idx, value in enumerate(height):
            
            while stk and height[stk[-1]] < value:
                bar = height[stk.pop()]
                if stk:
                    l, leftBound = stk[-1], height[stk[-1]]
                    minBound = min(value, leftBound)
                    res += (idx - l - 1) * (minBound - bar)
            
            stk.append(idx)

        return res




