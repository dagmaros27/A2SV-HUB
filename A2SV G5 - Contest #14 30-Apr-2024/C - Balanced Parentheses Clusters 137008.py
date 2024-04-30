# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

for _ in range(int(input())):
    n = int(input())
    b = input()
    
    hmap = {i:(i,1) for i in range((n)*2)}
    
    def find( x):
        while x != hmap[x][0]:
            x = hmap[hmap[x][0]][0]
        
        return x


    def union(x,y):
        xRep = find(x)
        yRep = find(y)
        
        if xRep != yRep:
            if hmap[xRep][1] >hmap[yRep][1]:
                size = hmap[xRep][1] + hmap[yRep][1]
                hmap[yRep] = [xRep,size]
                hmap[xRep] = [xRep,size]
            else:
                size = hmap[xRep][1] + hmap[yRep][1]
                hmap[yRep] = [yRep,size]
                hmap[xRep] = [yRep,size]
    
    opens = []
    for i in range(n*2):
        if b[i] == "(":
            opens.append(i)
        if b[i] == ")":
            v = opens.pop()
            union(i,v)
            if i +1  < 2*n and b[i+1]=="(":
                union(i,i+1)

    
    ans = 0
    for key in hmap:
        if key == hmap[key][0]:
            ans += 1
    print(ans)
                
    
    

            
            
            