# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [0]*n
        hmap = defaultdict(int)
        dp[0] = 1
        hmap[arr[0]] = 0

        for i in  range(1,n):
            if arr[i] - difference in hmap:
                dp[i] = 1 + dp[hmap[arr[i] - difference]]
            else:
                dp[i] = 1
            hmap[arr[i]] = i
        return max(dp)

        