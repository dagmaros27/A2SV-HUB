# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)

        for rich, poor in richer:
            graph[poor].append(rich)

        def bfs(root):
            visited = set()
            queue = deque([root])
            ans = root

            while queue:
                node = queue.popleft()
                if quiet[node] < quiet[ans]:
                    ans = node

                visited.add(node)

                for nbr in graph[node]:
                    if nbr not in visited:
                        queue.append(nbr)

            return ans

        ans = [i for i in range(len(quiet))]

        for i in range(len(quiet)):
            ans[i] = bfs(i)

        return ans