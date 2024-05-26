# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palindrome(arr):

            for w in arr:
                if w != w[::-1]:
                    return False
            return True

        def dp(idx,parts):
            if idx == len(s):
                if is_palindrome(parts):
                    ans.append(parts.copy())
                return 

            if parts:
                parts.append(parts.pop() + s[idx])
                dp(idx+1,parts )
                p = parts.pop()
                parts.append(p[:-1])
            parts.append(s[idx])
            dp(idx+1, parts)
            parts.pop()


            return  

        dp(0,[])
        return ans

        