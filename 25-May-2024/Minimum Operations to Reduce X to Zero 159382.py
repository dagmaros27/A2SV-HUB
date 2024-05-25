# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        #means the longest subarray that give total - x

        total = sum(nums)
        target = total - x
        if min(nums) > x or total < x:
            return -1
        l = 0 
        summ = 0
        mxm = 0
        get = False
        for r in range(len(nums)):
            summ += nums[r]
            while l < len(nums) and summ > target:
                summ -= nums[l]
                l += 1
            if summ == target:
                get = True
                mxm = max(mxm, r-l + 1)
                
        return len(nums) - mxm if get else -1

        