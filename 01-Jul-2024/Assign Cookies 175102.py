# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        i,j = 0,0
        counter = 0

        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j +=1
                counter += 1
            else:
                j += 1
                
        return counter

        
            
      