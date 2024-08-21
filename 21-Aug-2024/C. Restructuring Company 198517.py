# Problem: C. Restructuring Company - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/C

from collections import defaultdict
n, q = map(int, input().split())
hmap = {i: [i, i, i, 1] for i in range(n + 1)}  

def find(i):
    if i != hmap[i][0]:
        hmap[i][0] = find(hmap[i][0]) 
    return hmap[i][0]

def union(i, j):
    iRep = find(i)
    jRep = find(j)
    
    if iRep != jRep:
        size1, size2 = hmap[iRep][3], hmap[jRep][3]
        mnm = min(hmap[iRep][1], hmap[jRep][1])
        mxm = max(hmap[iRep][2], hmap[jRep][2])
        counter = size1 + size2
        
        if size1 >= size2:
            hmap[jRep][0] = iRep  
            hmap[iRep][1:] = [mnm, mxm, counter]
        else:
            hmap[iRep][0] = jRep  
            hmap[jRep][1:] = [mnm, mxm, counter]

def isTeam(i, j):
    return find(i) == find(j)

teams = defaultdict(int)
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        union(b, c)
    elif a == 2:
        curr = b
        if not teams[c]:
            teams[c] = c + 1

        while b <= c:
            union(b, curr)
            curr = b
            b = b + 1 if not teams[b] else teams[b]
            teams[curr] = teams[c]
            
    else:
        if isTeam(b, c):
            print("YES")
        else:
            print("NO")
