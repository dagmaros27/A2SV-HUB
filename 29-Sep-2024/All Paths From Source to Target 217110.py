# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        ans = []
        last = len(graph)-1

        def dfs(node,path):

            nonlocal ans

            path.append(node)    
            if last == node:
                ans.append(path.copy())
            
            for nbr in graph[node]:
                dfs(nbr,path.copy())

        dfs(0,[])
        return ans
            



            



        