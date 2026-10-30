class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        vis = [False] * numCourses
        path = [False] * numCourses

        def dfs(node):
            vis[node] = True
            path[node] = True
            for x in adj[node]:
                if not vis[x] and dfs(x):
                    return True
                elif path[x]:
                    return True
            path[node] = False
            return False
        
        for node in range(numCourses):
            if not vis[node] and dfs(node):
                return False
        return True