# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        func = lambda x : arr[x] < arr[x+1] 


        l,r = 0, len(arr)-1

        while l < r:
            m = (l+r)//2

            print(l,r)
            if  func(m):
                l = m+1
            else: r = m

        return l


        