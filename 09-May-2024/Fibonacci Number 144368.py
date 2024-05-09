# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:

    def fib(self, n: int) -> int:
        arr = [0]*31
        arr[1] = 1

        def rec(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if arr[n] :
                return arr[n]
            
            mem  =  self.fib(n-1) + self.fib(n-2)
            arr[n] = mem

            return mem
        
        return rec(n)
            