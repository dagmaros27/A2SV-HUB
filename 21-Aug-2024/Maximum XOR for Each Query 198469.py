# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ps = [0]* len(nums)
        ps[0] = nums[0]
        lim = 2**maximumBit
        
        for i in range(1,len(nums)):
            ps[i] = ps[i-1]^nums[i]
       
        ans = []
        for i in range(len(nums)):
            mxmK = ps[i]^(lim-1)

            ans.append(mxmK)

        return ans[::-1]

        