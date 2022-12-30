class Solution:
    def indexer(self, num):
        r = num//self.n
        c = num%self.n
        return r, c

    def get(self, matrix, idx):
        r, c = self.indexer(idx)
        return matrix[r][c]

    def search(self, matrix, num, low, high):
        if low == high:
            return False
        if low == high - 1:
            if self.get(matrix,low) == num:
                return True
            else:
                return False
        mid = low + (high-low)//2
        if num > self.get(matrix, mid):
            return self.search(matrix, num, mid, high)
        elif num < self.get(matrix, mid):
            return self.search(matrix, num, low, mid)
        else:
            return True

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.m = len(matrix)
        self.n = len(matrix[0])
        l = self.m*self.n
        return self.search(matrix, target, 0, l)
