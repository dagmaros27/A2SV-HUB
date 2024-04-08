# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh_count += 1

        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def inbound(i,j):
            return (0 <= i < len(grid)) and (0 <= j < len(grid[0]))
        def bfs():
            nonlocal fresh_count
            time = 0
            while queue and fresh_count:
                lvl = len(queue)
                while lvl:
                    print(queue)
                    row,col = queue.popleft()
                    for x ,y in dirs:
                        nx = row + x
                        ny = col + y
                        if inbound(nx,ny) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            queue.append((nx,ny))
                            fresh_count -= 1
                    lvl -= 1
                time += 1

            return time

        res = bfs()

        return res if fresh_count == 0 else -1



                
                



        