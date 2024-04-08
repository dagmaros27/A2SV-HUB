# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for _ in range(len(rooms))]

        queue = deque(rooms[0])
        visited[0] = True

        def bfs():

            while queue:
                print(queue)
                node = queue.popleft()
                visited[node] = True
                for i in rooms[node]:
                    if not visited[i]:

                        queue.append(i)
        bfs()
        return not visited.count(False)

                
        