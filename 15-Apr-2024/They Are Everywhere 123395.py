# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import Counter,defaultdict
n = int(input())
w = input()

c = len(Counter(w))
hmap = defaultdict(int)
l = 0
ans = float('inf')
for r in range(n):
    hmap[w[r]] += 1
    
    while len(hmap) > c:
        hmap[w[l]] -= 1
        if hmap[w[l]] == 0:
            del hmap[w[l]]
        l += 1
    while len(hmap) == c:
        ans = min(ans, r-l+1)
        hmap[w[l]] -= 1
        if hmap[w[l]] == 0:
            del hmap[w[l]]
        l += 1
        

print(ans)    
    
    
