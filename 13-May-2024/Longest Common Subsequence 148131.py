# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = [[-1 for i in range(len(text2))] for j in range(len(text1))]        
        def dp(t1,t2):
            if t1 ==len(text1) or t2 == len(text2):
                return 0

            if memo[t1][t2] != -1:
                return memo[t1][t2]
            
            if text1[t1] != text2[t2]:                
                memo[t1][t2] =  max( dp(t1+1,t2), dp(t1,t2+1))
            else:
                memo[t1][t2] = 1 + dp(t1+1,t2+1)
            
            return memo[t1][t2]

        return dp(0,0)

