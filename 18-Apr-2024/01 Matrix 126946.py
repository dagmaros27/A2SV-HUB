# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        def inbound(x,y): return (0 <= x < len(mat)) and (0 <= y < len(mat[0]))
        
        zeros = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    zeros.append((i,j))
                else:
                    mat[i][j] = -1
        

        queue = deque(zeros)

        while queue:
            x,y = queue.popleft()

            for dx,dy in moves:
                new_x = x + dx
                new_y = y + dy

                if inbound(new_x,new_y) and mat[new_x][new_y] == -1:
                    mat[new_x][new_y] = mat[x][y] +1
                    queue.append((new_x,new_y))


        return mat

        return ans

            
                
                    

        