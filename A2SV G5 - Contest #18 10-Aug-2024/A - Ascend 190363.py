# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n = int(input())
nums = list(map(int, input().split()))

c = 1
mxm = 1
for i in range(1,n):
    if nums[i] > nums[i-1]:
        c += 1
    else:
        c = 1
    mxm = max(mxm,c)
        
    
print(mxm)
