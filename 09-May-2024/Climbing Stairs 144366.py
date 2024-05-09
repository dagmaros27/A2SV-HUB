# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # one, two = 1,1

        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        # return one
        # #bottom up approach

        arr = [0]*46
        def rec(n):
            if n == 0:
                return 1
            if n <= 0:
                return 0
            if  arr[n]:
                return arr[n]
            
            res = rec(n-1) + rec(n-2)
            arr[n] = res

            return res
        return rec(n)


        