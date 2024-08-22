# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    
        dirs = [(0,1),(1,0),(-1,0),(0,-1), (1,1),(-1,-1),(-1,1),(1,-1)]


        def inbound(x,y):
            return (0 <= x < len(board)) and (0 <= y < len(board[0]))

        def dfs(row,col):

                if board[row][col] == "M":
                    board[row][col] = "X"
                    return
                
                bombs = 0

                for x,y in dirs:
                    new_x = row + x
                    new_y = col + y
                    if inbound(new_x,new_y):
                        if board[new_x][new_y] == "M":
                            bombs += 1
                board[row][col] = str(bombs) if bombs else "B" 
                if board[row][col] == "B":
                    for x,y in dirs:
                        new_x = row + x
                        new_y = col + y
                        if inbound(new_x,new_y) and board[new_x][new_y] == "E":
                            dfs(new_x,new_y)
                return 
        
        dfs(click[0],click[1])
        
        return board
            

        
        