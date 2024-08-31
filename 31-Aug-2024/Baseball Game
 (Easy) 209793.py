# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for i in operations:
            if i == "+":
                temp = stk[-1] + stk[-2]
                stk.append(temp)
            elif i == "D":
                stk.append(stk[-1]*2)
            elif i == "C":
                stk.pop()
            else:
                stk.append(int(i))
        
        return sum(stk)
        