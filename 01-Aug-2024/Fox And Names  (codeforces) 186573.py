# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque

n = int(input())
names = [input().strip() for _ in range(n)]

graph = defaultdict(set)
in_degree = defaultdict(int)
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(n - 1):
    w1, w2 = names[i], names[i + 1]
    min_len = min(len(w1), len(w2))
    for j in range(min_len):
        if w1[j] != w2[j]:
            if w2[j] not in graph[w1[j]]:
                graph[w1[j]].add(w2[j])
                in_degree[w2[j]] += 1
            break
    else:
        if len(w1) > len(w2):
            print("Impossible")
            exit()

queue = deque([ch for ch in alpha if in_degree[ch] == 0])
order = []

while queue:
    ch = queue.popleft()
    order.append(ch)
    for nei in graph[ch]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue.append(nei)

if len(order) != 26:
    print("Impossible")
else:
    print("".join(order))
