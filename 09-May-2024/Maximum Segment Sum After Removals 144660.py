# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        parent = [i for i in range(len(nums))]
        size = [n for n in nums]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        def union(x, y):
            u, v = find(x), find(y)
            if u != v:
                parent[u] = v
                size[v] += size[u]
                size[u] = 0
            
            
        ans = [0] * len(nums)
        temp = [0] * len(nums)
        for i in range(len(removeQueries) - 2, -1, -1):
            n = removeQueries[i + 1]
            temp[n] = nums[n]
            if n - 1 >= 0 and temp[n - 1] > 0:
                union(n - 1, n)
                
            if n + 1 < len(nums) and temp[n + 1] > 0:
                union(n, n + 1)
                
            ans[i] = max(ans[i + 1], size[find(n)])
        
        return ans
            
            
    