# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())
# or s > 10**(m+1)-1
if s == 0 :
    if m == 1:
        print(0,0)
        exit()
    print(-1, -1)
    exit()

# ans = []
# def backtrack(arr, curr, rem):
#     if rem == 0:
#         if curr == s and arr[0] != 0:
#             ans.append(arr.copy())
#         return
    
#     for i in range(10):
#         if curr + i > s:
#             break
#         arr.append(i)
#         backtrack(arr, curr + i, rem - 1)
#         arr.pop()

# backtrack([], 0, m)

# if not ans:
#     print(-1, -1)
# else:
#     ans.sort()

#     mnm = map(str, ans[0])
#     mxm = map(str, ans[-1])

#     print("".join(mnm), "".join(mxm))

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



        