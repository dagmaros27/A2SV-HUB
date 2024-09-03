# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

from math import gcd, log2, ceil

for _ in range(int(input())):
    n = int(input())

    mxm_val = (1 << int(ceil(log2(n + 1)))) - 1 
    if n == mxm_val:
        ans = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                ans = max(ans, i, n // i)
        print(ans)
    else:
        print(mxm_val)

