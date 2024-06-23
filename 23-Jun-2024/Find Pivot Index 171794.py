# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        total = sum(nums)
        for j in range(len(nums)):
            if lsum * 2 == total - nums[j]:
                return j
            lsum += nums[j]
        return -1