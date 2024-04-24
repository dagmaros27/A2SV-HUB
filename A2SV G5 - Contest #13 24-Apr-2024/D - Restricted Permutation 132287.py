# Problem: D - Restricted Permutation - https://codeforces.com/gym/519135/problem/D

from collections import defaultdict
from heapq import heappop, heappush, heapify

n, k = map(int, input().split())

graph = defaultdict(list)
pres = [0 for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    pres[b] += 1

ans = []
queue = [i for i in range(1, n + 1) if pres[i] == 0]
heapify(queue)
while queue:
    node = heappop(queue)
    ans.append(node)
    for nbr in graph[node]:
        pres[nbr] -= 1
        if pres[nbr] == 0:
            heappush(queue, nbr)

if len(ans) < n:
    print(-1)
else:
    print(*ans)