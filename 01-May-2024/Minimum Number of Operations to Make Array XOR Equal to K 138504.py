# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = reduce(lambda x, y: x ^ y, nums)

        resBin = bin(res)
        kBin = bin(k)

        counter = 0
        while k or res:
            if k%2 != res%2:
                counter += 1
            k //=2
            res //=2
        
        return counter