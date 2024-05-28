# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pf = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            pf.append(total)

        n = len(pf)-1
        mnm = inf
        ans = 0
        for i in range(len(pf)):
            first = (pf[i]//(i+1)) 
            last = ((pf[n] - pf[i])// (n-i)) if n-i > 0 else 0
            avgdif = abs(first - last)

            if avgdif < mnm:
                ans = i
                mnm = avgdif
        



        return ans
        