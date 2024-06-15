# Problem: C - Coffee Dilemma - https://codeforces.com/gym/528792/problem/C

import heapq

n = int(input())
arr = list(map(int, input().split()))

h = []
total = 0

for coffee in arr:
    total += coffee
    heapq.heappush(h, coffee)
    while total < 0:
        total -= heapq.heappop(h)

print(len(h))