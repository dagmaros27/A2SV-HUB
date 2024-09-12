# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mxm = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                mxm = max(mxm,curr)
                curr = 0
        mxm = max(mxm,curr)
        return mxm
        