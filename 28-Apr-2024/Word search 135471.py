# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        path = set() 

        def backtrack(x,y,idx):
            if idx == len(word): 
                return True
            
            if (x < 0 or y < 0 or x >= rows or y >= cols    
                or (x,y) in path or board[x][y] != word[idx]): 
                return False
            

            path.add((x,y))

            res = (backtrack(x+1,y,idx+1) or backtrack(x-1,y,idx+1) or 
                    backtrack(x,y+1,idx+1) or backtrack(x,y-1,idx+1))
            
            path.remove((x,y))

            return res

        for i in range(rows): 
            for j in range(cols):
                if backtrack(i,j,0): 
                    return True
        return False
        