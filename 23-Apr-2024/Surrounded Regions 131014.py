# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]

        def inbound(x,y): return (0 <= x < n) and (0 <= y < m)

        def onBorder(x,y): return x == 0 or x == n-1 or y == 0 or y == m-1

        #can be flliped only if the component doesnt have boardered "O"
        visited = set()
        def dfs(x,y):
            if onBorder(x,y):
                return False
            
            visited.add((x,y))
            valid  = True
            for dx,dy in dirs:
                nw_x = x + dx
                nw_y = y + dy
                if inbound(nw_x,nw_y) and board[nw_x][nw_y] == "O" and (nw_x,nw_y) not in visited:
                    valid = valid and dfs(nw_x,nw_y)

            return valid
        total = set()
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i,j) not in total:
                    valid = dfs(i,j)
                    if valid:
                        for x,y in visited:
                            board[x][y] = "X"
                    total.update(visited)
                    visited.clear()

        

             


        


        
        