# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        @cache

        def dp(i,bm):
            if i == len(nums1):
                return 0
            
            res = float("inf")

            for j in range(len(nums1)):
                if bm & (1<<j) == 0:
                    val = (nums1[i]^nums2[j]) + dp(i+1, bm | (1<<j) )
                    res = min(res, val )
            
            return res

        return dp(0,0)
    
        