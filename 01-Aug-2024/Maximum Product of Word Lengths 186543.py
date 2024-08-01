# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        masks = []

        for word in words:
            mask = 0
            for letter in word:
                mask |= 1 << (ord(letter) - ord("a"))
            
            masks.append(mask)

        for i in range(len(words)):
            for j in range(i+1,len(words)):         
                common = masks[i] & masks[j]
                if not common:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans