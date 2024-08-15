# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        ans = []
        merged = []
        for interval in intervals:
            if not merged:
                merged = interval
                continue
            else:
                if merged[1] >= interval[0]:
                    merged[1] = max(interval[1], merged[1])
                else:
                    ans.append(merged)
                    merged = interval
        ans.append(merged)
        return ans