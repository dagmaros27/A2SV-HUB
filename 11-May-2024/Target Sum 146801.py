# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        memo = {}
        count = 0

        def dp(i, curr):
            if i >= len(nums):
                if curr == target:
                    return 1
                return 0
            
            if (i,curr) not in memo:
                memo[(i,curr)] = dp(i+1,curr+nums[i]) + dp(i+1,curr- nums[i])
            return memo[(i,curr)]

        return dp(0,0)

            


        