# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        counter = 0

        for i in range(n):
            for j in range(m):


                if i == n-1 or i == 0 or j == m-1 or j == 0:
                    continue
                else:
                    d1 = sum([grid[i][j], grid[i+1][j+1], grid[i-1][j-1]])
                    d2 = sum([grid[i][j], grid[i+1][j-1], grid[i-1][j+1]])

                    r1 = sum([grid[i][j], grid[i+1][j], grid[i-1][j]])
                    r2 = sum([grid[i][j+1], grid[i+1][j+1], grid[i-1][j+1]])                
                    r3 = sum([grid[i][j-1], grid[i+1][j-1], grid[i-1][j-1]])
                    
                    c1 = sum([grid[i][j], grid[i][j-1], grid[i][j+1]])
                    c2 = sum([grid[i+1][j], grid[i+1][j-1], grid[i+1][j+1]])
                    c3 = sum([grid[i-1][j], grid[i-1][j-1], grid[i-1][j+1]])                   
                    setter = set()
                    if d1 != d2 or d2 != r1 or r1 != r2 or r2 != r3 or r3 != c1 or c1 != c2 or c2 != c3:
                        continue
                    for k in range(i-1, i+2):
                        for l in range(j-1, j+2):
                            if grid[k][l] > 9 or grid[k][l] == 0:
                                continue
                            setter.add(grid[k][l])
                    if len(setter) == 9:
                        counter += 1

        return counter