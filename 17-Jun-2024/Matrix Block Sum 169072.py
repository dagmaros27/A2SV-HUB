# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        pf = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                pf[i][j] = (mat[i - 1][j - 1] + pf[i - 1][j] + pf[i][j - 1] - pf[i - 1][j - 1])
        
        for i in range(n):
            for j in range(m):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(n, i + k + 1), min(m, j + k + 1)
                ans[i][j] = (pf[r2][c2] - pf[r1][c2] - pf[r2][c1] + pf[r1][c1])
        
        return ans