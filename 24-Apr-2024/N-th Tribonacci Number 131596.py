# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

@cache
class Solution:
    def tribonacci(self, n: int) -> int:
        def recur(n,dic):
            if n== 0:
                return 0
            if n== 1:
                return 1
            if n==2:
                return 1
            else:
                if n in dic:
                    return dic[n]
                else:
                    val = recur(n-1,dic) + recur(n-2,dic) + recur(n-3,dic) 
                    dic[n] = val
                    return val 
        return recur(n,defaultdict(int))
        