class Solution:
    def dfs(self,i,adj,visited):
        visited[i] = True
        for x in adj[i]:
            if not visited[x]:
                self.dfs(x,adj,visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*n
        ans = 0
        for node in range(n):
            if not visited[node]:
                self.dfs(node,adj,visited)
                ans+=1
        return ans