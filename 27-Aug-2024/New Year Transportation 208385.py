# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n,t = map(int, input().split())
arr = list(map(int, input().split()))
t -= 1
i = 0
while i < t:
    i += arr[i]

if i == t:
    print("Yes")
else:
    print("No")

