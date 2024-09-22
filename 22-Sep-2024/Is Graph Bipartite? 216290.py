# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        visited = set()

        def dfs(node, flag):
            if color[node] == flag:
                return False     
            elif color[node] == -1:
                color[node] = 0 if flag else 1
                visited.add(node)
                
                for n in graph[node]:
                    if n in visited and color[n] == color[node]:
                        return False
                    valid = dfs(n, color[node])
                    if not valid:
                        return False
            
                return True  
            else:
                return True
        ans = True
        
        for  i in range(len(graph)):
            if i not in visited:
                ans = ans and dfs(i,0)
        
        return ans