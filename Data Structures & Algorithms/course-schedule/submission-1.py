class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)

        visited= {i : 0 for i in range(numCourses)}
        
        def dfs(node):
            visited[node] =1
            for nei in graph[node]:
                if visited[nei]==1:
                    return False
                
                if visited[nei]==0:
                    if not dfs(nei):
                        return False
                
            visited[node]= 2
            return True
        
        for node in range(numCourses):
            if visited[node]==0:
                if not dfs(node):
                    return False
        return True
