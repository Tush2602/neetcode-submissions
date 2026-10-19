class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[v].append(u)

        visited ={i : 0 for i in range(numCourses)}
        order = []

        def dfs(node):
            visited[node] =1
            for nei in graph[node]:
                if visited[nei] ==1:
                    return False
                
                if visited[nei]==0:
                    if not dfs(nei):
                        return False
            visited[node] =2
            order.append(node)
            return True

        for node in range(numCourses):
            if visited[node]==0:
                if not dfs(node):
                    return []
                
        return order[::-1]