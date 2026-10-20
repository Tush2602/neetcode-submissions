from collections import deque 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        is_visited = [0 for _ in range(n)]
        cnt = 0
        for i in range(n):
            if is_visited[i] ==1:
                continue
            cnt+=1
            queue = deque()
            queue.append((i, -1))
            is_visited[i]=1

            while queue:
                node ,parent = queue.popleft()
                for nei in graph[node]:
                    if is_visited[nei] == 0:
                        queue.append((nei, node))
                        is_visited[nei] =1
                    else:
                        if nei != parent:
                            continue
        return cnt 


