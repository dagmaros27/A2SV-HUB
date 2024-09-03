# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        setter = set()
        mxm = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] in setter:
                change = mxm - nums[i]
                change += 1
                ans += change
                new_num = nums[i] + change
                setter.add(new_num)
                mxm = max(mxm,new_num)
            else:
                setter.add(nums[i])
                mxm = max(nums[i], mxm)

                
        return ans