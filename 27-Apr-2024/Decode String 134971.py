# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:

    def decodeString(self, s: str) -> str:
        
        def decode(s, i):
            res = ''
            n = 0
            while i<len(s):
                if s[i].isdigit():
                    n = n*10+int(s[i])
                elif s[i]=='[':
                    decoded, i = decode(s, i+1)
                    res += n*decoded
                    n = 0
                elif s[i]==']': 
                    return res, i
                else:
                    res += s[i]
                i += 1

            return res, i

        return decode(s, 0)[0]
                