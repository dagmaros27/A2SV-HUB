# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution: 
    def fib(self, n: int) -> int: 
        memo = [0] * (n + 1) 
        def _fib(n): 
            if n == 0 or n == 1:  
                return n 
             
            if not memo[n]: 
                memo[n] = _fib(n - 1) + _fib(n - 2) 
             
            return memo[n] 
         
        return _fib(n)