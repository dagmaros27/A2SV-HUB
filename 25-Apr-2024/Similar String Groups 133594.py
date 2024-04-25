# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isIdentical(x,y):
            counter =0
            for i in range(len(x)):
                if x[i] != y[i]:
                    counter += 1
            return counter <= 2

        rep = {i:i for i in strs}

        def find(x):
            while x != rep[x]:
                x = rep[rep[x]]
            return x
        
        def union(x,y):
            xRep = find(x)
            yRep = find(y)

            if xRep != yRep:
                rep[yRep] = xRep
        
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i != j and isIdentical(strs[i],strs[j]):
                    union(strs[i],strs[j])
        res = 0
        for key in rep:
            if key == rep[key]:
                res += 1

        return res


        