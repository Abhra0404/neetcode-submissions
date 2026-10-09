class Solution:
    def dfs(self,i,j,grid):
        n = len(grid)
        m = len(grid[0])
        if i<0 or j<0 or i>=n or j>=m:
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(i+1,j,grid)
        self.dfs(i-1,j,grid)
        self.dfs(i,j+1,grid)
        self.dfs(i,j-1,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.dfs(i,j,grid)
                    ans+=1
        return ans