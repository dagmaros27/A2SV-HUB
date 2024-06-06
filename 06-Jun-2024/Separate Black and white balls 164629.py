# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        zeros = 0
        ans = 0
        
        for right in range(len(s)-1,-1,-1):
            if s[right] == '0':
                zeros += 1
            if s[right] == '1':
                ans += zeros
        
        return ans
