# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max = strs[0]

        for i in range(1,len(strs)):
            if len(strs[i]) < len(max):
                max = max[:len(strs[i])]
            for j in range(len(strs[i])):
                if j < len(max) and strs[i][j] != max[j]:
                    max = max[:j]
                    break
        return max
            
        