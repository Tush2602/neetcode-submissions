from collections import deque 
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False 
        graph = {i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = deque()
        is_visited = [0 for _ in range(n)]
        for i in range(n):
            if is_visited[i] ==1:
                continue 
            queue.append((i,-1))
            is_visited[i] =1

            while queue:
                node, parent = queue.popleft()
                for nei in graph[node]:
                    if is_visited[nei]==0:
                        is_visited[nei] =1
                        queue.append((nei, node))
                    else:
                        if nei != parent:
                            return False 
        return True 