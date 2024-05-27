# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:

        setter = set()
        counter = 1

        for i in range(len(s)):
            if s[i] in setter:
                counter += 1
                setter.clear()
            setter.add(s[i])
        return counter

        