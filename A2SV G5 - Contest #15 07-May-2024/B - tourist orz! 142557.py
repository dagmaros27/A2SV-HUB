# Problem: B - tourist orz! - https://codeforces.com/gym/522079/problem/B

for _ in range(int(input())):
    a,b = map(int, input().split())
    nums = list(map(int, input().split()))
    
    mxm = b
    
    for n in nums:
        mxm = max(mxm, b|n,n)
    
    print(mxm)
    
    
    
