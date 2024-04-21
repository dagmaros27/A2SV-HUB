# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

from typing import List
from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(set)
        deps = defaultdict(set)

        for u, v in prerequisites:
            graph[u].add(v)
            deps[v].add(u)

        mat = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        def dfs(node, start):
            mat[start][node] = True

            for nbr in graph[node]:
                if not mat[start][nbr]:
                    dfs(nbr, start)

        for i in range(numCourses):
            dfs(i, i)

        ans = []
        for u, v in queries:
            ans.append(mat[u][v])

        return ans