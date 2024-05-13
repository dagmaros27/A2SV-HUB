# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        hmap = {}

        def find(x):
            if x not in hmap:
                hmap[x]=x
            if x != hmap[x]:
                hmap[x] = find(hmap[x])
            return hmap[x]
    
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            hmap[root_x] = hmap[root_y]
        
        for frm, to, dist in roads:
            union(frm, to)

        res = float('inf')
        for frm, to, dist in roads:
            if find(1) == find(frm):
                res = min(res, dist)
        
        return res