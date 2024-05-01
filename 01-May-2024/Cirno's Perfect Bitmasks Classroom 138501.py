# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

for _ in range(int(input())):
    n = int(input())
    ans = 1
    ns = bin(n)
    i = -1
    if n==1: 
        print(3) 
        continue
    while i > -(len(ns)-2) and ns[i] != "1":
        ans = ans<<1
        i -= 1
    if i == -(len(ns)-2):
        m = 1
        while n & m:
            n = n & (~m)
            m = m << 1
        n = n | m
        print(n)
    else:
        print(ans)
            