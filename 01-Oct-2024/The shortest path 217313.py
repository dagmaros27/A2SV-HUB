# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque
n,m = map(int,input().split())
a,b = map(int,input().split())
graph = defaultdict(list)
relations = defaultdict(int)

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque()
visited = set()
queue.append(a)
visited.add(a)
relations[a] = -1

def bfs():

    while queue:
        node = queue.popleft()
        if node == b:
            return
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.add(n)
                relations[n] = node

bfs()
ans = []


if relations[b] == 0:
    print(-1)
else:
    child = b

    while child != -1:
        ans.append(child)
        child = relations[child]

    ans.reverse()
    print(len(ans)-1)
    print(*ans)
