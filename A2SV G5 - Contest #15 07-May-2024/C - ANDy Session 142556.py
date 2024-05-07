# Problem: C - ANDy Session - https://codeforces.com/gym/522079/problem/C

import math
for _ in range(int(input())):
    a,b = map(int, input().split())
    nums = list(map(int, input().split()))
    
    bits = [0]*31
    
    for n in nums:
        w = 1
        p = 0
        while n:
            if n&w:
                bits[p] += 1
            
            p += 1
            n >>= 1
    
    l_nums = len(nums)
    
    ans = 0
    for i in range(30,-1,-1):
        if bits[i] + b >= l_nums:
            b -= (l_nums - bits[i])
            ans += 1<<i
    print(ans)
            
        