# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hmap = {i: [i, 0] for i in range(n)}

        def find(x):
            if x == hmap[x][0]:
                return x
            hmap[x][0] = find(hmap[x][0])
            return hmap[x][0]

        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            size1, size2 = hmap[xRep][1], hmap[yRep][1]
            if xRep != yRep:
                size = size1 + size2
                if size1 > size2:
                    hmap[yRep] = [xRep, size]
                else:
                    hmap[xRep] = [yRep, size]

        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        
        
        ans = [None] * len(queries)
        idx = 0
        for w, p, q, i in queries: 
            while idx < len(edgeList) and edgeList[idx][0] < w: 
                _, u, v = edgeList[idx]
                union(u, v)
                idx += 1
            ans[i] = find(p) == find(q)
        return ans