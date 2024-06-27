# Problem: D - Max of Max - https://codeforces.com/gym/530187/problem/D

def check(max_val):

    for i in range(n):

        cost = 0
        cur_val = max_val
        for j in range(i, n):
            
            if a[j] < cur_val and j == n - 1:
                cost = k + 1
                break
            
            if a[j] >= cur_val:
                break

            cost += cur_val - a[j]
            next_val = max(cur_val - 1, 0)
            cur_val = next_val

        if cost <= k:
            return True

    return False



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    low = max(a)
    high = max(a) + min(k, n)

    while low <= high:

        mid = low + (high - low)//2

        if check(mid):
            low = mid + 1
        
        else:
            high = mid - 1
    
    print(high)