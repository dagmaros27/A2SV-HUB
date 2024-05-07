# Problem: A - a-e-i-o-u-y - https://codeforces.com/gym/522079/problem/A

n = int(input())
w = input()
vowels = set(['a','e','i','o','u','y'])
prevv = False

i=1
while i < len(w):
    if w[i-1] in vowels and w[i] in vowels:
        w = w[:i] + w[i+1:]
        i -= 1
    i += 1

print(w) 