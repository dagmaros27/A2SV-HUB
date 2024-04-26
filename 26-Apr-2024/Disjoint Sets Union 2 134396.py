# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n,q = map(int, input().split())
hmap = {i : [i,i,i,1] for i in range(n+1)}


def find(i):
    while i != hmap[i][0]:
        i = hmap[hmap[i][0]][0]
    return i
    
def union(i,j):
    iRep = find(i)
    jRep = find(j)
    
    if iRep != jRep:
        size1,size2 = hmap[iRep][3], hmap[jRep][3]
        mnm = min(hmap[iRep][1],hmap[jRep][1])
        mxm = max(hmap[iRep][2],hmap[jRep][2])
        counter = size1 + size2
        if size1 > size2:
            hmap[jRep] = [iRep,mnm,mxm,counter]
            hmap[iRep] = [iRep,mnm,mxm,counter]       
        else:
            hmap[jRep] = [jRep,mnm,mxm,counter]
            hmap[iRep] = [jRep,mnm,mxm,counter]
        
        
        
        
        

for _ in range(q):
    arr = list(input().split())
    if arr[0] == "union":
        union(int(arr[1]),int(arr[2]))
    else:
        rep = find(int(arr[1]))
        print(* hmap[rep][1:])
        
        
        