# Problem: A - Balanced Alphabet - https://codeforces.com/gym/519135/problem/A

alpha = "abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
    a,b = map(int, input().split())
    
    words = list(alpha[:b])
    ans = []
    for i in range(a):
        ans.append(words[i%b])
    
    print("".join(ans))
    
    
    