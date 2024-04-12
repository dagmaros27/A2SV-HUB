# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        graph = defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    for x, y in dirs:
                        if inbound(i + x, j + y) and grid[i + x][j + y] == 0:
                            graph[(i, j)].append((i + x, j + y))

        queue = deque([(0, 0, 1)]) 
        visited = set()

        while queue:
            x, y, path_length = queue.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return path_length

            for neighbor_x, neighbor_y in graph[(x, y)]:
                queue.append((neighbor_x, neighbor_y, path_length + 1))

        return -1