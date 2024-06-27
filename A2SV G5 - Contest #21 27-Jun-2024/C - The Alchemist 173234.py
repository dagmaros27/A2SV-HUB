# Problem: C - The Alchemist - https://codeforces.com/gym/530187/problem/C

import sys
from collections import defaultdict, deque
input = sys.stdin.readline
def solve():
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    nums = set(map(int, input().split()))

    graph = defaultdict(list)
    degree = [0] * (n + 1)
    future = [0] * (n + 1)
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        m, edges = line[0], line[1:]
        if i in nums:
            continue
        degree[i] = m
        for a in edges:
            graph[a].append(i)

    stack = []
    for node in range(1, n + 1):
        if node in nums:
            stack.append(node)
        elif degree[node] == 0:
            ans[node] = cost[node]
            stack.append(node)

    while stack:
        node = stack.pop()
        for child in graph[node]:
            degree[child] -= 1
            future[child] += ans[node]
            if degree[child] == 0:
                stack.append(child)
                ans[child] = min(cost[child], future[child])

    print(*ans[1:])

q = int(input())
for _ in range(q):
    solve()