# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # A triangle is valid if sum of its two sides is greater than the third side.

        # def validSides(num1,num2,num3):
        #     return num1+num2 > num3 and num1+num3 > num2 and num2+num3 > num1
        # maxParam = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i != j and j != k and i != k:
        #                 if validSides(nums[i],nums[j],nums[k]):
        #                     param = sum([nums[i],nums[j],nums[k]])
        #                     maxParam = max(maxParam,param)
                    
        # return maxParam
        #a very long answer TLE

        nums.sort()
        maxParam = 0

        for  i in range(len(nums)-1,1,-1):
            if nums[i] < nums[i-2] + nums[i-1]:
                maxParam = max(maxParam, nums[i] + nums[i-1]+ nums[i-2])

        return maxParam

    
        