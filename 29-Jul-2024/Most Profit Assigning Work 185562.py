# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        def bs( mxmP, target):
            left, right = 0, len(mxmP) - 1
            while left <= right:
                mid = (left + right) // 2
                if mxmP[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        jobs = sorted(zip(difficulty, profit))
        
        max_profit_for_difficulty = []
        max_profit = 0
        
        for d, p in jobs:
            max_profit = max(max_profit, p)
            max_profit_for_difficulty.append((d, max_profit))
        
        total_profit = 0
        for w in worker:
            index = bs(max_profit_for_difficulty, w)
            if index >= 0 and w >= max_profit_for_difficulty[index][0]:
                total_profit += max_profit_for_difficulty[index][1]
        
        return total_profit
    
