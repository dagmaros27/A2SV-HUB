# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpha = [0]*26

        for i in t:
            alpha[ord(i) - ord('a')] += 1
        
        for i in s:
            alpha[ord(i) - ord('a')] -= 1

        for i in range(26):
            if alpha[i] == 1:
                return chr(97 + i)

        

        