from collections import deque 
class Solution:
    def dfs(self, node, parent, graph, is_visited):
        is_visited[node]= True
        for nei in graph[node]:
            if not is_visited[nei]: 
                is_visited[nei] =True
                self.dfs(nei, node, graph, is_visited)
        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i :[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        is_visited = [False] * n
        cnt = 0
        for i in range(n):
            if is_visited[i] == True:
                continue 
            cnt+=1
            self.dfs(i, -1, graph, is_visited)

        return cnt

