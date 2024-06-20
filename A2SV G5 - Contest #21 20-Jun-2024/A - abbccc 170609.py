# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n = int(input())
w = input()
ans = [w[0]]
diff = 1
i = 0
while i + diff < n:
    i += diff
    ans.append(w[i])
    diff += 1
    
print("".join(ans))
    
