# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x = 0

        for i in nums:
            x = x^i

        return x


        
        