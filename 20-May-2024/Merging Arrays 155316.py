# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
i,j = 0,0
while i < n and j < m:
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
        ans.append(arr2[j])
        j += 1
        
while i < n:
    ans.append(arr1[i])
    i += 1
while j < m:
    ans.append(arr2[j])
    j += 1

print(*ans)