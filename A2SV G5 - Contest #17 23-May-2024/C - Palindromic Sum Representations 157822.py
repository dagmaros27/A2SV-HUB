# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

import sys
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def generate_palindromes_up_to(n):
    palindromes = []
    for i in range(1, n + 1):
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes

def main():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    queries = [int(data[i]) for i in range(1, t + 1)]
    
    max_query = max(queries)
    palindromes = generate_palindromes_up_to(max_query)
    
    mod = 10**9 + 7
    
    dp = [0] * (max_query + 1)
    dp[0] = 1
    
    for coin in palindromes:
        for i in range(coin, max_query + 1):
            dp[i] = (dp[i] + dp[i - coin]) % mod
    
    for n in queries:
        print(dp[n])

main()
