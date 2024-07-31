# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hmap = defaultdict(int)
        max_num = 0

        l = 0

        for r in range(len(fruits)):
            hmap[fruits[r]] += 1
            
            while len(hmap) > 2:
                hmap[fruits[l]] -= 1
                if hmap[fruits[l]] == 0:
                    del hmap[fruits[l]]
                l += 1
            max_num = max(max_num, sum(hmap.values()))
        
        return max_num