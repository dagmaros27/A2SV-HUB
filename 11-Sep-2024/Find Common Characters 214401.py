# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alpha = [float('inf')]*26
        ans = []
        len_words = len(words)
        for idx in range(len_words):
            for i in range(26):
                letter = chr(ord("a") + i)
                if letter not in words[idx]:
                    alpha[i] = -1
                else:
                    if alpha[i] != -1:
                        alpha[i] = min(words[idx].count(letter), alpha[i])
        
        for i in range(26):
            if alpha[i] > 0:
                letter = chr(ord("a") + i)
                ans.extend([letter]* alpha[i])

        
                  
        return ans