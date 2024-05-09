# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        p = 1
        ans = 0
        for i in range(left.bit_length()):
            if p &left != 0 and p&right != 0 :
                if p^right < left:
                    ans += p
            p <<= 1
        return ans
                


                
                

        
        