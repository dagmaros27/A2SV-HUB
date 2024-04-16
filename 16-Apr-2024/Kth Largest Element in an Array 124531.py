# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        
        while k and nums:
            heappush(arr,nums.pop())
            k -= 1
        while nums:
            heappush(arr,nums.pop())
            heappop(arr)
        return heappop(arr)
        