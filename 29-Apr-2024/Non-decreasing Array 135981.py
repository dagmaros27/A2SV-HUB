# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # it is true :
        # if one big element at the begining 
        # if one small element at the end
        # if one peak or hole in between
        # if it is non decreasing already

        i = 0
        modify = -1
        counted = 0
        while i< len(nums)-1:
            if nums[i] > nums[i+1]:
                counted += 1
                modify = i
            i += 1
        
        print(modify)
        if modify == -1:
            return True
        if counted < 2:
            if modify == 0 or modify == len(nums)-2:
                return True
            elif nums[modify-1] <= nums[modify+1]:
                return True
            elif modify+2 < len(nums) and nums[modify] <= nums[modify+2]:
                return True
            else:
                return False
            
        else:
            return False



            
        
              