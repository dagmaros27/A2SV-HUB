# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1, rob2 = 0,0
        # for every triple [rob1,rob2,n]
        # for n in nums:51
        #     temp = max(rob1+n, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        
        # return rob2
        memo = [-1] * len(nums)
    
        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if memo[i] != -1:
                return memo[i]
            
            res = max(dp(i - 1), dp(i - 2) + nums[i])
            memo[i] = res
            
            return res
        
        return dp(len(nums) - 1)







        