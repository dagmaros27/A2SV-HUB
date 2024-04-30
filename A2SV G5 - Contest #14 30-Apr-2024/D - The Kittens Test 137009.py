# Problem: D - The Kittens Test - https://codeforces.com/gym/520688/problem/D

n = int(input())

rep = {}

group = [[] for _ in range(n + 1)]


for i in range(1, n + 1):

    group[i].append(i)
    rep[i] = i

size = [1] * (n + 1)


def find(x):

    if rep[x] != x:
        rep[x] = find(rep[x])

    return rep[x]


def union(x, y):
    xx = find(x)
    yy = find(y) 
    jls = yy
    if xx != jls:

        if size[xx] >  size[yy]:
            rep[yy] = xx

            group[xx].extend(group[yy])

            size[xx] += size[yy]

        else:
            rep[xx] = yy

            group[yy].extend(group[xx])

            size[yy] += size[xx]

for _ in range(n - 1):

    x, y = map(int, input().split())

    union(x, y)


print(*group[find(1)])