# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
if s == 0 :
    if m == 1:
        print(0,0)
        exit()
    print(-1, -1)
    exit()

mxm = []
 
for i in range(m):
    if s > 9:
        mxm.append(9)
        s -= 9
    else:
        mxm.append(s)
        s -= s
    
mnm = list(reversed(mxm))
 
nonzero = 0
 
while mnm[nonzero] == 0:
    
    nonzero += 1
 
mnm[0] += 1
mnm[nonzero] -= 1
 
if s == 0:
                
    mnm = map(str, mnm)
    mxm = map(str, mxm)
 
 
    print("".join(mnm), "".join(mxm))
else:
    print(-1, -1)