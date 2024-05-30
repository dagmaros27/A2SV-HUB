# Problem: Sum of Distances - https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = defaultdict(list)
        ans = [0]*len(nums)
        for idx, val in enumerate(nums):
            dic[val].append(idx)

        for key,val in dic.items():
            suff = sum(val)
            pre = 0
            sLen = len(val)
            pLen = 0

            for i in val:
                pre += i
                suff -= i
                pLen += 1
                sLen -= 1
                ans [i] = (-pre+pLen*i - sLen*i+suff) 
        return ans

        
        