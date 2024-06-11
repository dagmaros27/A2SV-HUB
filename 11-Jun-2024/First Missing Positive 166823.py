# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        while i < len(nums):
            
            if nums[i]-1 != i:
                val = nums[i]
                if val <= 0 or val > len(nums) or nums[val-1] == val:
                    i += 1
                    continue
                nums[i], nums[val-1] = nums[val-1],nums[i]
            
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i]-1 != i:
                return i+1
        
        return nums[-1]+1 