# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = []
        negative = []
        for i in nums:
            if i > 0:
                postive.append(i)
            else:
                negative.append(i)
            
        i = 0 
        j = 1

        while i < len(negative):
            postive.insert(j, negative[i])
            j += 2
            i += 1
        

        return postive
