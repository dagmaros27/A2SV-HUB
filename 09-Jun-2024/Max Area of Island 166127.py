# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(0,-1), (1,0), (-1,0)]

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(x,y):
            return (0 <= x < len(grid)) and (0 <= y < len(grid[0]))
        
        def dfs(row,col):
            
            visited[row][col] = True
            area = 1

            for x,y in dirs:
                new_row = row + x
                new_col = col + y

                if inbound(new_row,new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == 1:
                    
                    area += dfs(new_row,new_col)

            return area


        res = 0

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, dfs(i,j))
        
        return res

            
        
                

        