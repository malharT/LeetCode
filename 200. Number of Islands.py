class Solution:
    def dfs(self, grid, row, col):
        if ((row < 0 or row == len(grid)) or
           (col < 0 or col == len(grid[0])) or
           (grid[row][col] != '1')):
            return
        else:
            grid[row][col] = 'v'
        self.dfs(grid, row+1, col)
        self.dfs(grid, row-1, col)
        self.dfs(grid, row, col+1)
        self.dfs(grid, row, col-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count