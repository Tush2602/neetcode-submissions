from typing import List

class Solution:
    def dfs(self, node, parent, visited, graph):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                if self.dfs(nei, node, visited, graph):
                    return True

            elif nei != parent:
                return True

        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        if self.dfs(0, -1, visited, graph):
            return False

        return all(visited)