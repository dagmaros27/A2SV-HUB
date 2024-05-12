# Problem: X-Sum - https://codeforces.com/contest/1676/problem/D

def bishop_attack(i,j,matrix):
    n = len(matrix)
    m = len(matrix[0])
    a,b = i,j
    sum = 0
    #left diagonal down
    while 0 <= a < n and 0 <= b < m:
        sum += matrix[a][b]
        a += 1
        b += 1

    
    a,b = i,j
    #left diagonal up
    while 0 <= a < n and 0 <= b < m:
        sum += matrix[a][b]
        a -= 1
        b -= 1
    
    
    #right diagonal down
    a,b = i,j
    while 0 <= a < n and 0 <= b < m:
        sum += matrix[a][b]
        a += 1
        b -= 1
     #right diagonal up
    a,b = i,j
    while 0 <= a < n and 0 <= b < m:
        sum += matrix[a][b]
        a -= 1
        b += 1
    num = matrix[i][j] * 3
    
    sum -= num
    return sum

tests = int(input())

for _ in range(tests):
    
    n,m = list(map(int, input().split()))
    mat = [list(map(int, input().split())) for i in range(n)]
    maxSum = 0
    for i in range(n):
        for j in range(m):
            sum = bishop_attack(i,j,mat)
            maxSum = max(maxSum, sum)
    
    print(maxSum)

