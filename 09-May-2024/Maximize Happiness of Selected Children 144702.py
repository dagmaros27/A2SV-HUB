# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        
        turn = 0
        ans = 0
        for i in range(len(happiness)-1,len(happiness)-k-1,-1):
            if happiness[i] - turn >0:
                ans += (happiness[i] - turn)
            turn += 1
        return ans


        