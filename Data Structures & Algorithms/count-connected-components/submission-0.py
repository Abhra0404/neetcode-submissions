class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False]*n
        ans = []
        def dfs(node):
            visited[node] = True
            comp.append(node)
            for n in adjList[node]:
                if not visited[n]:
                    dfs(n)
        for node in range(n):
            if not visited[node]:
                comp = []
                dfs(node)
                ans.append(comp)
        return len(ans)