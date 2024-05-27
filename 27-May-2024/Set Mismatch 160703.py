# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missed = 0
        setter = set()

        for i in nums:
            if i in setter:
                missed = i
            setter.add(i)
        dupped = (n * (n+1))//2 - sum(setter) 

        return [missed,dupped]
        

        