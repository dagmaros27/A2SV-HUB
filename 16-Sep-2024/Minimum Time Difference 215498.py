# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        
        for time in timePoints:
            h,m = time.split(":")
            h = int(h) * 60
            m = int(m)
            arr.append(h+m)

        for i in range(len(timePoints)):
            arr.append(arr[i]+1440)
        arr.sort()

        print(arr)


        mnm = float('inf')
        
        for i in range(1,len(arr)):
            mnm = min(mnm, arr[i]- arr[i-1])
        return mnm


        