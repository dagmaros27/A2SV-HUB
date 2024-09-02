# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        visited1 = set()
        visited2 = set()
        n, m = len(grid1), len(grid1[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def inbound(x, y): 
            return 0 <= x < n and 0 <= y < m
            
        def dfs(visited, grid, x, y):
            island = set()
            stack = [(x, y)]
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) in visited or grid[cx][cy] == 0:
                    continue
                visited.add((cx, cy))
                island.add((cx, cy))
                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy
                    if inbound(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 1:
                        stack.append((nx, ny))
            return island

        coord1 = set()

        for i in range(n):
            for j in range(m):
                if grid1[i][j] == 1 and (i, j) not in visited1:
                    island = dfs(visited1, grid1, i, j)
                    coord1.update(island)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1 and (i, j) not in visited2:
                    sub_island = dfs(visited2, grid2, i, j)
                    if sub_island.issubset(coord1):
                        ans += 1

        return ans