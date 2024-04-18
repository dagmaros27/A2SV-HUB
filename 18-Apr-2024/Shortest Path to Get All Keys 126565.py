# Problem: Shortest Path to Get All Keys - https://leetcode.com/problems/shortest-path-to-get-all-keys/


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n, m = len(grid), len(grid[0])
        queue= deque()
        visited= set()
        keys= set()
        all_keys = set()
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inbound(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < m
        
        start = (0, 0)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].islower():
                    all_keys.add(grid[i][j])
        
        queue.append((start[0], start[1], 0, ""))
        visited.add((start[0], start[1], ""))
        
        while queue:
            row, col, path, collected = queue.popleft()
            
            if len(collected) == len(all_keys):
                return path
            
            for dx, dy in moves:
                x = row + dx
                y = col + dy
                curr = grid[x][y] if inbound(x, y) else '#'
                
                if curr == '#':
                    continue
                
                if curr.isupper() and curr.lower() not in collected:
                    continue
                
                key = collected
                if curr.islower() and curr not in collected:
                    key += curr
                
                if (x, y, key) not in visited:
                    queue.append((x, y, path + 1, key))
                    visited.add((x, y, key))
        
        return -1