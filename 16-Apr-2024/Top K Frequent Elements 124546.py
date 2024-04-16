# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key = lambda x: x[1])
        ans = []
        while k:
            ans.append(counter.pop()[0])
            k -= 1
        return ans

        