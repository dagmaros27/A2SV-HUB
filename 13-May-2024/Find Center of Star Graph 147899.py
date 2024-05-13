# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        table = [0] * (len(edges)+2)

        for a,b in edges:
            table[a] += 1
            table[b] += 1
        
        return table.index(len(edges))
        