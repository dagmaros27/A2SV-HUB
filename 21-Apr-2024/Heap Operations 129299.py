# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq
from collections import defaultdict
n = int(input())
ops = []
arr = []

ans = []
heapq.heapify(arr)
hmap = defaultdict(int)
for _ in range(n):
    op = input().split()
    if op[0] == "insert":
        heapq.heappush(arr, int(op[1]))
        ans.append(op)
    elif op[0] == "removeMin":
        if  arr:
            mnm = heapq.heappop(arr)
        else:
            ans.append(["insert",0])
        ans.append(op)
    elif op[0] == "getMin":

        while arr and arr[0] < int(op[1]):
            mnm = heapq.heappop(arr)
            ans.append(["removeMin"])
                   
                
        if not arr or arr[0] != int(op[1]):
            ans.append(["insert", op[1]]) 
            heapq.heappush(arr,int(op[1]))
        ans.append(["getMin", op[1]])
        
print(len(ans))
for op in ans:
    print(*op)
    
