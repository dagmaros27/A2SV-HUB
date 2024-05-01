# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x ^= y
        counter = 0

        while x:
            x &= x-1
            counter += 1

        return counter
        