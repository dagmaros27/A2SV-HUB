# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ops = len(nums)-1
        ans = []
        zeros = 0
        
        for i in range(ops):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
        for num in nums:
            if num > 0:
                ans.append(num)
            else:
                zeros += 1
        while zeros:
            ans.append(0)
            zeros -= 1
        
        return ans
        