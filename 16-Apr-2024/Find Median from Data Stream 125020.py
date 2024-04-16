# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minh = []
        self.maxh = []
        

    def addNum(self, num: int) -> None:
        if len(self.maxh) == 0 or num < -self.maxh[0]:
            heappush(self.maxh, -num)
        else:
            heappush(self.minh, num)

        if len(self.maxh) < len(self.minh):
            heappush(self.maxh, - heappop(self.minh))
        elif len(self.maxh) - len(self.minh) > 1:
            heapq.heappush(self.minh , -heappop(self.maxh))

    def findMedian(self) -> float:
        if len(self.maxh) == len(self.minh):
            return (self.minh[0]- self.maxh[0])/2
        else:
            return -self.maxh[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()