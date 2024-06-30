# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        hmap = {i: 0 for i in range(len(edges))}

        for i in range(len(edges)):
            hmap[edges[i]] += i

        hmap = sorted(hmap.items(), key=lambda x: x[1],reverse=True)
        return hmap[0][0]