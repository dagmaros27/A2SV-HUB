# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        mxm = ''
        
        def dfs(word):
            nonlocal mxm            
            if word in memo: return memo[word]                        
            
            curr_len = 0
            
            if word == '':
                curr_len = 0                
            elif word[:-1] in words_set:
                curr_len = 1 + dfs(word[:-1])                                
            else:
                curr_len = float('-inf')                
            
            if curr_len > len(mxm) or (curr_len == len(mxm) and word < mxm):                
                mxm = word
                        
            memo[word] = curr_len
            return curr_len
            
        
        words_set = set(words)
        words_set.add('')
        memo = {}
        
        for word in words:
            dfs(word)
            
        return mxm
        