# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(len(nums)+2):
        #     if i in nums:
        #         pass
        #     else:
        #         return i

        # # n = len(nums)
        # # sum = ((n)*(n+1)) // 2
        # # for i in nums:
        # #   sum -= i
        
        # # return sum

        # i = 0
        # nums.append(-1)

        # while i < len(nums):
        #     if nums[i] != i:
        #         val = nums[i]
        #         if val == -1:
        #             i += 1
        #             continue
        #         nums[i], nums[val] = nums[val],nums[i]
        #     else:
        #         i += 1
        
        # return nums.index(-1)


        # nums.sort()

        # for i in range(len(nums)):
        #     if i ^ nums[i]:
        #         return i
        
        # return len(nums)

        rge = 0
        arr = 0

        for idx,num in enumerate(nums):
            arr ^= num
            rge ^= idx+1

        return arr^rge
        