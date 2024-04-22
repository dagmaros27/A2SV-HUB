# Problem: Shifting Letters - https://leetcode.com/problems/shifting-letters/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shifts.reverse()
        for i in range(1,len(shifts)):
            shifts[i] += shifts[i-1]
        
        shifts.reverse()
        ans = []
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(s)):
            idx = alpha.index(s[i])

            idx = (idx + (shifts[i])%26)%26
            ans.append(alpha[idx])

        return "".join(ans)
            


        