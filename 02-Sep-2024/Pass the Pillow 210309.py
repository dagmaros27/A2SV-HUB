# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        k = 1  

        while time > 0:
            while k < n and time > 0: 
                k += 1
                time -= 1
            while k > 1 and time > 0:  
                k -= 1
                time -= 1

        return k
