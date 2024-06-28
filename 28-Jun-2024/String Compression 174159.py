# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = None
        cnt = 0
        i = 0

        for cur in chars + ['']:
            if cur != prev and cnt:
                chars[i] = prev
                i += 1
                if cnt > 1:
                    for digit in str(cnt):
                        chars[i] = digit
                        i += 1
                cnt = 0
            prev = cur
            cnt += 1
        
        return i