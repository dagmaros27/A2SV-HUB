# Problem: Minimum Number of Operations to Move All Balls to Each Box - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        for i in range(len(boxes)):
            ops = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == "1":
                    ops += abs( int(i) - int(j))
            ans.append(ops)

        return ans 
        