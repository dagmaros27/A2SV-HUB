# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        row1 = set( "qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        for word in words:
            x = set(word.lower())
            if x.issubset(row1) or x.issubset(row2) or x.issubset(row3):
                ans.append(word)
        

        return ans
