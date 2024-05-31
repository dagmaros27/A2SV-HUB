# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        order = []
        color = ["W" for _ in range(len(graph))]
        

        def dfs(node):
            if color[node] == "G":
                return False
            
            if color[node] == "B": 
                return True
            
            color[node] = "G"

            valid = True
            for nbr in graph[node]:
                valid = valid and dfs(nbr)
            
            if valid:
                color[node] = "B"
                order.append(node)
                return True
            else:
                return False
        
        for i in range(len(graph)):
            if color[i] == "W":
                dfs(i)
        
        order.sort()
        
        return order
            
        
        
        