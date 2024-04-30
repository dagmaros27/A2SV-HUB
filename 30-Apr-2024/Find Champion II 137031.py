# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        # hmap = {i:i for i in range(n)}

        # def find(x):
        #     while x != hmap[x]:
        #         x = hmap[hmap[x]]
        #     return x
        
        # def union(x,y):
        #     xRep = find(x)
        #     yRep = find(y)

        #     if xRep != yRep:
        #         hmap[yRep] = xRep
        

        # for u,v in edges:
        #     union(u,v)

        # ans = []
        # for k in  hmap:
        #     if k == hmap[k]:
        #         ans.append(k)
        # print(ans)
        # return ans[0] if len(ans) == 1 else -1


        pres = {i : [] for i in range(n)}
        for u,v in edges:
            pres[v].append(u)

        ans = []

        for k in pres:
            if len(pres[k]) == 0:
                ans.append(k)

        return ans[0] if len(ans) == 1 else -1
            
        