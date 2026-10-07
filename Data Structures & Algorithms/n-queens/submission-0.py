class Solution:
    def isSafe(self,board,row,col,n):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i in range(1, min(row, col) + 1):
            if board[row - i][col - i] == 'Q':
                return False
        for i in range(1, min(row, n - 1 - col) + 1):
            if board[row - i][col + i] == 'Q':
                return False
        return True

        
    def nQueens(self,board,row,n,ans):
        if row == n:
            ans.append(["".join(r) for r in board])
            return
        for i in range(n):
            if self.isSafe(board,row,i,n):
                board[row][i] = "Q"
                self.nQueens(board,row+1,n,ans)
                board[row][i] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        self.nQueens(board,0,n,ans)
        return ans