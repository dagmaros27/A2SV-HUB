# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)

        pres = [0 for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            pres[v] += 1
        
        queue = deque()
        for i in range(n):
            if pres[i] == 0:
                queue.append((i))
        
        
        ans = [[] for _ in range(n)]

        while queue:
            n = queue.popleft()

            for nbr in graph[n]:
                pres[nbr] -= 1
                heappush(ans[nbr], n)
                for par in ans[n]:
                    if par not in ans[nbr]:
                        heappush(ans[nbr], par)

                if pres[nbr] == 0:
                    queue.append(nbr)
        
        res = []

        for i in ans:
            arr = []
            while i:
                arr.append(heappop(i))
            res.append(arr)

        return res


        





        