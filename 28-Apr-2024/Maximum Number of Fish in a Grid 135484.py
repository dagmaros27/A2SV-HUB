# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        moves = [(0,1),(1,0),(-1,0),(0,-1)]


        def inbound(x,y): return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        visited = set()
        def dfs(x,y):
            
            total = grid[x][y]

            visited.add((x,y))

            for dx,dy in moves:
                xx = x + dx
                yy = y + dy
                if inbound(xx,yy) and (xx,yy) not in visited and grid[xx][yy] != 0:
                    total += dfs(xx,yy)
            
            return total
        mxm = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i,j) not in visited:
                    mxm = max(dfs(i,j), mxm)

        return mxm