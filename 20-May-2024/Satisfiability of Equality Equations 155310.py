# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
            
            alpha = "abcdefghijklmnopqrstuvwxyz"
            rep = {i: i for i in alpha}


            def find(x):
                while x != rep[x]:
                    x = rep[x]
                return x
            
            def union(x,y):
                xRep = find(x)
                yRep = find(y)

                if xRep < yRep:
                    rep[yRep] = xRep
                else:
                    rep[xRep] = yRep
            
            def connected(x,y):
                return find(x) == find(y)
            

            for eq in equations:
                if eq[1] == "=":
                    union(eq[0],eq[3])
            
            for eq in equations:
                if eq[1] == "!":
                    if connected(eq[0],eq[3]):
                        return False
      

            return True
        