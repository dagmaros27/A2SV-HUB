# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """     
        rows=defaultdict(set)
        cols=defaultdict(set)
        blocks=defaultdict(set)
        
        seen=deque()
     
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    blocks[(i//3,j//3)].add(board[i][j])
                else:             
                    seen.append((i,j))    
        
        def dfs():         
            if not seen:
                return True         
            r,c=seen.popleft()         
            b=(r//3,c//3)
            
            for num in {"1","2","3","4","5","6","7","8","9"}:                
                if num not in rows[r] and num not in cols[c] and num not in blocks[b]:
                    board[r][c]=num                   
                    rows[r].add(num)
                    cols[c].add(num)                 
                    blocks[b].add(num)
                    if dfs():
                        return True                    
                    board[r][c]="."                    
                    rows[r].discard(num)                   
                    cols[c].discard(num)
                    blocks[b].discard(num)                
            seen.appendleft((r,c))
            
            return False
        
        dfs()
                    
                    
                
                
            
                
                
                
        