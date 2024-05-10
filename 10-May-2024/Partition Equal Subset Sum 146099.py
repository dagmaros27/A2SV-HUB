# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        memo = {}

        def dp(i , target):
            if i >= len(nums) :
                return target == 0
            
            if (i , target) not in memo:
                memo[(i , target)]= dp(i + 1 , target - nums[i]) or dp(i + 1 , target)

            return memo[(i , target)]

        return dp( 0 , sum(nums) // 2)
        