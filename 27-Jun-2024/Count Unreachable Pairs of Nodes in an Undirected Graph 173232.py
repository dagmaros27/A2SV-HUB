# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        rep = {}

        def find(x):
            if x not in rep:
                rep[x] = x
            if x != rep[x]:
                rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            xRep = find(x)
            yRep = find(y)
            if xRep != yRep:
                rep[yRep] = xRep
        
        for i in range(n):
            rep[i] = i

        for u, v in edges:
            union(u, v)
        
        groups = defaultdict(int) 

        for i in range(n):
            groups[find(i)] += 1
        
        size = list(groups.values())
        total = n * (n - 1) // 2

        group_sum = sum(size * (size - 1) // 2 for size in size)
        
        ans = total - group_sum

        return ans