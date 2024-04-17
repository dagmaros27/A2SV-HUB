# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = []
    arr = [(-talk,idx+1) for idx,talk in enumerate(nums)]
    heapq.heapify(arr)
    
    one = heapq.heappop(arr)
    two = heapq.heappop(arr)
    
    while one[0] != 0 and two[0] != 0:
        
        onetalk,oneidx = one
        one = (onetalk+1,oneidx)
        
        twotalk,twoidx = two
        two = (twotalk+1,twoidx)
        
        ans.append((oneidx,twoidx))
        
        heapq.heappush(arr,one)
        heapq.heappush(arr,two)
        
        one = heapq.heappop(arr)
        two = heapq.heappop(arr)
    
    
    print(len(ans))
    
    for one,two in ans:
        print(one,two)

    