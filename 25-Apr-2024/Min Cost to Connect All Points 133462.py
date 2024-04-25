# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def md(x1,y1,x2,y2): return abs(x1-x2) + abs(y1-y2)
        
        hmap = {}
        for  i in range(len(points)):
            for j in range(len(points)):
                hmap[(i,j)] = md(points[i][0],points[i][1],points[j][0],points[j][1])

        hmap = sorted(hmap.items(), key= lambda x: x[1])
        rep = {i:i for i in range(len(points))}

        def find(x):
            while x != rep[x]:
                x = rep[rep[x]]
            return x
        def union(x,y):
            xRep = find(x)
            yRep = find(y)

            if xRep != yRep:
                rep[yRep] = xRep
        
        def isConnected(x,y):
            return find(x) == find(y)

        ans = 0
        ps = 0
        for coords,dist in hmap:
            p1,p2 = coords
            if not isConnected(p1,p2):
                union(p1,p2)
                ans += dist
            if ps == len(points)-1:
                break


        return ans   
            
        


            

        