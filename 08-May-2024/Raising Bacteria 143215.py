# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

n = int(input())
ans = 0
while n:
    if n&1:
       ans += 1 
    n >>= 1

print(ans)