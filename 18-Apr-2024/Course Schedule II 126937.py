# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        deg = [0 for i in range(numCourses)]

        for i in prerequisites:
            deg[i[0]] += 1
        
        graph = defaultdict(list)
        print(deg)
        for dep,nodep in prerequisites:
            graph[nodep].append(dep)
        
        queue =deque()

        for i in range(numCourses):
            if deg[i]== 0:
                queue.append(i)

        order = []

        while queue:
            node = queue.popleft()
            order.append(node)

            for nbr in graph[node]:
                deg[nbr] -= 1
                if deg[nbr] == 0:
                    queue.append(nbr)
        

        return order if len(order) == numCourses else []

        