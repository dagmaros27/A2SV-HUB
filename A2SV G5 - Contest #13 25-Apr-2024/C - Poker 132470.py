# Problem: C - Poker - https://codeforces.com/gym/519135/problem/C

from heapq import heappop, heappush
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    heap = []
    ans = 0
    for i in range(n):
        if nums[i] != 0:
            heappush(heap,-nums[i])
        else:
            if heap:
                ans += heappop(heap)
    print(abs(ans))
                