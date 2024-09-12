# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for i in range(n-2)] for i in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                mxm = 0
                for k in range(3):
                    for l in range(3):
                        mxm = max(grid[i+k][j+l],mxm)
                
                ans[i][j] = mxm
            

        return ans
        