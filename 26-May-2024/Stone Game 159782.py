# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(f,b):
            if f > b:
                return 0
            alice_turn = (b-f-len(piles))%2
            if alice_turn == 1:
                return max(piles[f]+dp(f+1,b), piles[b] + dp(f,b-1))
            else:
                return min(-piles[f] + dp(f+1,b),-piles[b] + dp(f,b-1))


        return dp(0,len(piles)-1) > 0


            
            

        