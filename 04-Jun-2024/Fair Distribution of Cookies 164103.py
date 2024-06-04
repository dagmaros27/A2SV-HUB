# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # avg = sum(cookies)//k
        # if len(cookies) == k:
        #     return max(cookies)
        def backtrack(cookie):
            nonlocal mnm
            if cookie >= len(cookies):
                mnm = min(mnm, max(dist))
                return 

            # if max(dist) > mnm:
            #     return

            for child in range(k):
                    
                if dist[child] + cookies[cookie] > mnm:
                    continue
                dist[child] += cookies[cookie]
                # if dist[child] > avg:
                #     continue
           
                backtrack(cookie+1)
                dist[child] -= cookies[cookie]
            
            return mnm
        
        mnm = float('inf')
        dist = [0]*k
        backtrack(0)

        return mnm