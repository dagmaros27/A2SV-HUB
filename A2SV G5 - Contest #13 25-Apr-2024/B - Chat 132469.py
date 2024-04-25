# Problem: B - Chat - https://codeforces.com/gym/519135/problem/B

from heapq import heapify, heappop, heappush, nlargest
n,k,q = map(int, input().split())

nums = list(map(int, input().split()))

heap = []

for i in range(q):
    a,b = map(int, input().split())
    if a == 1:
        heappush(heap, (nums[b-1], b-1))
        
        if len(heap) > k:
            heappop(heap)
    else:
        if (nums[b-1],b-1) in heap:
            print("YES")
        else:
            print("NO")




