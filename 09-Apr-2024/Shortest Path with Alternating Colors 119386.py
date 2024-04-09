# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for s,d in redEdges:
            red[s].append(d)

        for s,d in blueEdges:
            blue[s].append(d)
        
        ans = [-1] * n
        ans[0] = 0

        queue = deque()
        queue.append([0,0,None])

        visit = set()
        visit.add((0,None))     

        while queue:
            node,length,color = queue.popleft()
            if ans[node] == -1:
                ans[node] = length
            if color != "R":
                for n in red[node]:
                    if (n,"R") not in visit:
                        queue.append((n,length+1,"R"))
                        visit.add((n,"R"))

            if color != "B":
                for n in blue[node]:
                    if (n,"B") not in visit:
                        queue.append((n,length+1,"B"))
                        visit.add((n,"B"))

        return ans

                



        