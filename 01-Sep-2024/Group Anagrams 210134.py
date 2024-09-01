# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for str1 in strs:
            count  = [0]*26 # to count the occurrence of each character
            for i in str1:
                count[ord(i) - ord("a")]+=1 # offset the chars assci to 0-25
            answer[tuple(count)].append(str1)
        return list(answer.values())
