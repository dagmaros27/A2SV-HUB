# Problem: African Crossword - https://codeforces.com/problemset/problem/90/B

n,m = map(int, input().split())
mat =[]

for _ in range(n):
    mat.append(list(input()))
   
cross_out = set()
for row in range(n):
    for col in range(m):
        if mat[row].count(mat[row][col]) >1 and (row,col) not in cross_out:
            cross_out.add((row,col))

for col in range(m):
    column_row = [mat[row][col] for row in range(n)]
    for row in range(n):
        if column_row.count(mat[row][col]) >1 and (row,col) not in cross_out:
            cross_out.add((row,col))
        

ans = []
for row in range(n):
    for col in range(m):
        if (row,col)  in cross_out:
            mat[row][col] = ""
for row in range(n):
    for col in range(m):
        if  mat[row][col]:
           ans.append(mat[row][col])
           
print("".join(ans))

       
        

