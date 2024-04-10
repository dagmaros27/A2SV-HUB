# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

def merge(left, right):
    count = 0  
    if left[0] > right[0]:
        count += 1  
        return left + right, count
    return right + left, count

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0  

    m = len(arr) // 2
    left, left_count = mergeSort(arr[:m])
    right, right_count = mergeSort(arr[m:])

    merged, count = merge(left, right)
    return merged, count + left_count + right_count

for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    sorted_x,count = mergeSort(x)
    ans = list(reversed(sorted_x))

    if ans == sorted(x):
        print(count)
    else:
        print(-1)