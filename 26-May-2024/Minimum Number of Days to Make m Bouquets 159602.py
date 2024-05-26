# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        l, h = 0, max(bloomDay)
        
        def f(num):
            cons = 0
            busq = 0
            for day in bloomDay:
                if day <= num:
                    cons += 1
                    if cons == k:
                        busq += 1
                        cons = 0
                else:
                    cons = 0
            return busq >= m
        
        while l < h:
            mid = (l + h) // 2
            if f(mid):
                h = mid
            else:
                l = mid + 1
        
        return l