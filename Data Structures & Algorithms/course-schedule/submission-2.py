from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        indegrees = [0 for v in range(numCourses)]

        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] +=1

        queue = deque()
        result= []

        for i in range(numCourses):
            if indegrees[i] ==0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in graph[node]:
                indegrees[nei]-=1
                if indegrees[nei]==0:
                    queue.append(nei)

        return len(result) == numCourses