# Problem: D - Medina & Merbebt - https://codeforces.com/gym/522079/problem/D

def pf_bits(arr):
    pf = [[0] * 32]
    bits = [0] * 32
    
    for n in arr:
        w = 1
        p = 0
        
        while n:
            if n & w:
                bits[p] += 1
            p += 1
            n >>= 1
        
        pf.append(bits.copy())
    
    return pf


def getRangeAnd(l, r, arr):
    ans = 0
    
    for i in range(32):
        sets = arr[r][i] - arr[l - 1][i] 
        if sets == r - l + 1:
            ans += (1 << i)
    
    return ans


def bs(l, k, arr):
    left = l
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if getRangeAnd(l, mid, arr) >= k:
            left = mid + 1
        else:
            right = mid - 1

    return right if right >= l else -1


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    q = int(input())
    
    pf = pf_bits(nums)
    
    ans = []
    for _ in range(q):
        l, k = map(int, input().split())
        
        query = bs(l, k, pf)
        ans.append(query)
    
    print(*ans)