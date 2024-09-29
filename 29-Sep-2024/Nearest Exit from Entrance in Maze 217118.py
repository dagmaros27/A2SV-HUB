# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = len(maze), len(maze[0])
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        def is_inbound(x, y):
            return 0 <= x < row and 0 <= y < col

        def is_end(x, y):
            return (x == 0 or y == 0 or x == row - 1 or y == col - 1)

        def bfs():
            q = deque([[entrance[0], entrance[1], 0]])
            visited = set()
            visited.add(tuple(entrance))

            while q:
                x, y, lvl = q.popleft()
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if is_inbound(nx, ny) and maze[nx][ny] == '.' and (nx, ny) not in visited:
                        if is_end(nx, ny) and [nx, ny] != entrance:
                            return lvl + 1
                        visited.add((nx, ny))
                        q.append([nx, ny, lvl + 1])

            return -1

        return bfs()
