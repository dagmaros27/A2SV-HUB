# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        setter = set(list(allowed))
        ans = 0
        for word in words:
            word_set = set(list(word))

            if word_set.issubset(setter):
                ans += 1
        
        return ans
