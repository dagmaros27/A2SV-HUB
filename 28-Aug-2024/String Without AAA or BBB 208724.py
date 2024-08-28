# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        a_turn = 0
        b_turn = 0

        while a or b:
            if (max(a,b) == a or b_turn == 2) and a_turn < 2:
                ans.append("a")
                a -=1
                a_turn += 1
                b_turn = 0 
            else:
                if b_turn < 2:
                    ans.append("b")
                    b -= 1
                    b_turn += 1
                    a_turn = 0


        return "".join(ans)
        
        