# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

word1 = input().lower()
word2 = input().lower()


if word1 < word2:
    print(-1)
elif word2 < word1:
    print(1)
else:
    print(0)