# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        rep = {i:i for i in range(1,len(edges)+1)}
        ans = []
            
        def union( x,y ):
            xRep = find(x)
            yRep = find(y)

            if xRep != yRep:
                rep[yRep] = xRep

        def find(x):
            while x != rep[x]:
                x = rep[x]
            
            return x
        def isConnected(x,y):
            return find(x) == find(y)
        
        for x,y in edges:
            con = isConnected(x,y)
            if con:
                ans = [x,y]
            else:
                union(x,y)

        
        return ans
    


        