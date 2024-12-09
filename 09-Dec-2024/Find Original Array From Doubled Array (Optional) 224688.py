# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2:
            return []
        
        #bruteforce

        changed.sort()
        res = []
        wanted = {}

        s1 = 0

        while s1 < n:
            if changed[s1] in wanted:
                wanted[changed[s1]] -= 1
                if wanted[changed[s1]] == 0:
                    del wanted[changed[s1]]
                res.append(changed[s1]//2)
                s1 += 1
                continue
            wanted[changed[s1]*2] = wanted.get(changed[s1]*2, 0) +1
            s1+= 1
        
        if len(wanted) > 0:
            return []
        else:
            return res


        
