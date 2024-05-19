# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        else:
            
            setter = set()
            dic = {}

            for i in range(len(s)):
                
                if s[i] in dic:
                    if dic[s[i]] != t[i] :
                        return False
                else:
                    if t[i] in setter:
                        return False
                    dic[s[i]] = t[i]
                    setter.add(t[i])

            return True



            