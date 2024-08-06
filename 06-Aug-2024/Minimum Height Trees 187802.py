# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        pres = [0] * n
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            pres[u] += 1
            pres[v] += 1
        
        queue = deque()

        for i in range(n):
            if pres[i] == 1:
                queue.append(i)
        
        e = n
        while queue and e > 2:
            e -= len(queue)
            
            for _ in range(len(queue)):
                n = queue.popleft()

                for v in graph[n]:
                    pres[v] -= 1
                    
                    if pres[v] == 1:
                        queue.append(v)

        return list(queue) if edges else [0]





        