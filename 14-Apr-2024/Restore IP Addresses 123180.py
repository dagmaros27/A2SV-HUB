# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start = 0, segments=[]):
            if len(segments) == 4:
                if start == len(s):
                    result.append(".".join(segments))
                return
            
            for digit in range(1, 4):
                if start + digit > len(s): break

                segment = s[start:start+digit]
                if (digit > 1 and segment.startswith('0')) or int(segment) > 255: continue

                segments.append(segment)
                backtrack(start+digit, segments)
                segments.pop()
        
        backtrack()
        return result