# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        i,j = 0, len(nums)-1
        counter = 0
        indexes = set()
        while i < j:

            if nums[i] + nums[j] == k:
                if i in indexes:
                    i +=1
                    continue
                if j in indexes:
                    j -=1
                    continue
                counter += 1
                indexes.add(i)
                indexes.add(j)
                i += 1
                j -= 1

            elif nums[i] + nums[j] > k:
                j -= 1
                
            else:
                i += 1
        
        return counter