# Problem: F - OR Encryption - https://codeforces.com/gym/543431/problem/F

for _ in range(int(input())):
    n = int(input())
    mat = []
    for _ in range(n):
        nums = list(map(int, input().split()))
        mat.append(nums)
      
    a = [2**30 - 1] * n
    
    for i in range(n):
        for j in range(n):
            if i != j:
                a[i] &= mat[i][j]
                a[j] &= mat[i][j]

    flag = False
    for i in range(n):
        for j in range(n):
            if i != j and a[i] | a[j] != mat[i][j]:
                print("NO")               
                flag = True
            if flag:
                break
        if flag:
            break
    if flag:
        continue
            
    print("YES")
    print(*a)