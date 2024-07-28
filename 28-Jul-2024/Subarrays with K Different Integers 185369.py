# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:     
        return self.atmost(nums, k) - self.atmost(nums, k - 1)
    
    def atmost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        i, j = 0, 0
        freq = Counter()

        while j < n:
            freq[nums[j]] += 1
            while i <= j and len(freq) > k:
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
                i += 1
            count += j-i+1
            j += 1

        return count