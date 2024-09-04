# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        num = []

        def add_digit(num):
            if len(num) == 1:
                return num
            
            ans = 0
            
            for n in num:
                ans += int(n)       
            
            return str(ans)
        
        for i in s:
            d = ord(i) - ord('a') +1
            num.append(str(d))

        number = "".join(num)

        while k:
            number = add_digit(number)
            k -= 1
        
        return int(number)