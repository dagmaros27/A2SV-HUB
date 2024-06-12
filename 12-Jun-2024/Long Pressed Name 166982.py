# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        i, j = 0, 0

        if len(name) > len(typed):
            return False
        
        while i < len(name) and j < len(typed):
            
            if name[i] == typed[j]:
                j += 1
                i += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        while j < len(typed) and typed[j] == typed[j-1]:
            j += 1

        return i == len(name) and j == len(typed)
