# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # store = Counter(supplies)
        # graph = defaultdict(int)
        # pres = [0 for i in range(len(recipes))]

        # for i in range(len(recipes)):
        #     pres[i] = len(ingredients)

        store = set(supplies)
        visited = set()
        ans = []
        
        def dfs(idx):
            valid = True
            visited.add(idx)
            for ing in ingredients[idx]:
                if ing in store:
                    continue
                elif ing in recipes:
                    rep_idx = recipes.index(ing)
                    if rep_idx not in visited:
                        valid = valid and dfs(rep_idx)
                        if not valid:
                            return False
                    else:
                        return False
                else:
                    return False
            store.add(recipes[idx])
            ans.append(recipes[idx])
            return True
        for i in range(len(recipes)):
            if i not in visited:
                dfs(i)
            
        return ans

        