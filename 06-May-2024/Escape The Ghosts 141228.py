# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        nearest = [float("inf"), float("inf")]

        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) < nearest[0] + nearest[1]:
                nearest  = [abs(ghost[0] - target[0]), abs(ghost[1] - target[1])]
        
        if abs(nearest[0]) + abs(nearest[1]) <= abs(target[0]) + abs(target[1]):
            return False
        else:
            return True

