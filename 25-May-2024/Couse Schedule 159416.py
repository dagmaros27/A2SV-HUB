# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0]*numCourses
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
            indeg[b] += 1
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)

        order = []
        while q:
            n = q.popleft()

            order.append(q)

            for nbr in graph[n]:
                indeg[nbr] -= 1
                if indeg[nbr] == 0:
                    q.append(nbr)

        
        return len(order) == numCourses



        