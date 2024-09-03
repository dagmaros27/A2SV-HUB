# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:        
        if n*m != len(original):
            return []
        
        mat = []  
        off = 0
        while off < len(original):
            row = []
            for i in range(n):
                row.append(original[off+i])
            mat.append(row)
            off += n
        
        return mat
        


            