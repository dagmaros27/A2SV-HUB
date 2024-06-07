# Problem: B - Eba loves math. - https://codeforces.com/gym/527294/problem/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    ans = nums[0]
    
    for num in nums:
        ans &= num
    
    print(ans)  