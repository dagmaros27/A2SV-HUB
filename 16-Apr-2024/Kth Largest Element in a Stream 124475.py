# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        i = k
        self.k = k
        self.arr = []
        
        while i and nums:
            heappush(self.arr,nums.pop())
            i -= 1
        while nums:
            heappush(self.arr,nums.pop())
            heappop(self.arr)
    
  

    def add(self, val: int) -> int:
        heappush(self.arr,val)
        if len(self.arr) > self.k:
            heappop(self.arr)
        ans = heappop(self.arr)
        heappush(self.arr,ans)
        

        return ans
   



        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)