from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u]+=1

        queue = deque()
        result = []

        for i in range(numCourses):
            if indegree[i] ==0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)

        return result if len(result) == numCourses else []
            
