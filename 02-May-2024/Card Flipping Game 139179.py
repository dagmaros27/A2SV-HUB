# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        unique = set(fronts + backs)

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                unique.discard(fronts[i])
        if len(unique) == 0:
            return 0
        return min(unique)

# Example usage:
# param_1 = [1, 2]
# param_2 = [2, 1]
# ret = Solution().flipgame(param_1, param_2)
# print(ret)
