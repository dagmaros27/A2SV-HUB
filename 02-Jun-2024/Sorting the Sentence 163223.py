# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        ss=  [(i[:-1], i[-1]) for i in s.split()]
        
        ss.sort(key = lambda x: x[1])

        return " ".join([i[0] for i in ss])


