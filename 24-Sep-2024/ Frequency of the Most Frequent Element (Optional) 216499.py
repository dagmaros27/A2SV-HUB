# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total = 0
        mxm = 1
        
        for r in range(1, len(nums)):
            total += (nums[r] - nums[r-1]) * (r - l)
            
            while total > k:
                total -= nums[r] - nums[l]
                l += 1

            mxm = max(mxm, r - l + 1)

        return mxm
