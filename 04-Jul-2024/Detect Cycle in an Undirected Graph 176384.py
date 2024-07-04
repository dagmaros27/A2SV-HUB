# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

from typing import List

class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        vis = [False] * V
        
        for i in range(V):
            if not vis[i]:  
                if self.dfsCycle(i, -1, adj, vis):
                    return True
                
        return False
    
    def dfsCycle(self, node: int, parent: int, adj: List[List[int]], vis: List[bool]) -> bool:
        vis[node] = True  
        
        for neighbour in adj[node]:  
            if not vis[neighbour]:  
                if self.dfsCycle(neighbour, node, adj, vis):
                    return True
            elif neighbour != parent:  
                return True
                
        return False