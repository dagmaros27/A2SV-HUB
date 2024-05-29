# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
           return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        return self.myPow(x,n//2) * self.myPow(x,n//2)*self.myPow(x,n%2)

        