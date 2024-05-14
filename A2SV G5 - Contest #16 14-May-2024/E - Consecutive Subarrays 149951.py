# Problem: E - Consecutive Subarrays - https://codeforces.com/gym/523525/problem/E

n, k = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
arr = []
for i in range(n - 1, -1, -1):
    sum += a[i]
    if i > 0:
        arr.append(sum)

res = sum

arr.sort(reverse=True)

for i in range(k - 1):
    res += arr[i]

print(res)