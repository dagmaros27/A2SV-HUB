# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
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
            
            for i in range(len(s1)):
                union(s1[i], s2[i])
            
            ans = []
            for char in baseStr:
                ans.append(find(char))
            
            return "".join(ans)
            
            
            
        