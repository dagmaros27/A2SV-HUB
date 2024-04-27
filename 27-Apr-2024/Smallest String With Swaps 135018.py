# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        hmap = {i : [i,1] for i in range(len(s))}

        def find( x):
            if x == hmap[x][0]:
                return x
            hmap[x][0] = find(hmap[x][0])
            return hmap[x][0]

        def union(x,y):
            xRep = find(x)
            yRep = find(y)
            size1,size2 = hmap[xRep][1], hmap[yRep][1]
            if xRep != yRep:
                size = size1 + size2
                if size1 > size2:
                    hmap[yRep] = [xRep,size]
                else:
                    hmap[xRep] = [yRep,size]


        for u,v in pairs:
            union(u,v)

        
        group = defaultdict(list)

        for key in hmap:
            heappush(group[find(key)],(s[key]))
        
        ans = []

        print(group)
        for i in range(len(s)):
            mnm = heappop(group[find(i)])
            ans.append(mnm)
        

        return "".join(ans)
       
        


        

        