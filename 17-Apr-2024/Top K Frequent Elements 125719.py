# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        arr = [(-count, n) for n,count in counter.items()]

        heapify(arr)
        ans = []

        for _ in range(k):
            ans.append(heappop(arr)[1])
            
        return ans
        