class Solution:
    def dfs(self, board, r, c, protect):
        if (r < 0 or r == len(board)
            or c < 0 or c == len(board[0])
            or (r,c) in protect
            or board[r][c] == 'X'):
            return
        protect.add((r,c))
        self.dfs(board, r+1, c, protect)
        self.dfs(board, r, c+1, protect)
        self.dfs(board, r-1, c, protect)
        self.dfs(board, r, c-1, protect)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        protect = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, protect)
            if board[i][n-1] == 'O':    
                self.dfs(board, i, n-1, protect)
        for i in range(n):
            if board[0][i] == 'O':
                self.dfs(board, 0, i, protect)
            if board[m-1][i] == 'O':
                self.dfs(board, m-1, i, protect)
        for i in range(m):
            for j in range(n):
                if (i,j) not in protect:
                    board[i][j] = 'X'