# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import defaultdict,deque
for _ in range(int(input())):
    n,k = map(int, input().split())
    
    graph = defaultdict(list)
    pres = [0]*(n+1)
    for _ in range(k):
        d,a,b = map(int, input().split())
        graph[a].append((d,b))
        if d == 1:
            pres[b] += 1
    
    queue = deque()  
    for i in range(n+1):
        if pres[i] == 0 and i != 0:
            queue.append(i)
            
        
    
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for d,nbr in graph[node]:
            if d== 1:
                pres[nbr] -= 1
                if pres[nbr] == 0:
                    queue.append(nbr)
    if len(order) != n:
        print("NO")
    else:
        print("YES")
        hmap = {order[i]: i for i in range(len(order))}

        
        for node in graph:
            for d,nbr in graph[node]:
                if d == 0:
                    if  hmap[node] > hmap[nbr]:
                        print(nbr,node)
                    else:
                        print(node,nbr)
                        
                else:
                    print(node,nbr)         
    
    
    

        
    