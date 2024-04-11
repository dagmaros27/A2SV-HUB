# Problem: Remove K Digits - https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        if len(num) == k:
            return "0"

        for i in num:
            while stk and int(stk[-1]) > int(i):
                if k:
                    stk.pop()
                    k -= 1
                else:
                    break
            stk.append(i)
        
        while k:
            stk.pop()
            k -= 1



        stk.reverse()

        while stk:
            if stk[-1] == "0":
                stk.pop()
            else:
                break
        
        stk.reverse()

        return "".join(stk) if stk else '0'
            
        