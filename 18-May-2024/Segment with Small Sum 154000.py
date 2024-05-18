# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n,s = list(map(int, input().split()))
nums = list(map(int, input().split()))

longest = 0
sum = 0
l = 0

for r in range(n):
    sum += nums[r]
    
    while sum > s:
        sum -= nums[l]
        l += 1
    longest = max(longest, r-l+1)

print(longest)
